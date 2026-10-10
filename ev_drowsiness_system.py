import cv2
import mediapipe as mp
import serial
import time

# CHANGE COM3 if your Arduino uses a different port
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

model_path = "face_landmarker.task"

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE,
    num_faces=1
)

# Eye landmark indices
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def eye_ratio(points, indices, width, height):
    p = []
    for i in indices:
        lm = points[i]
        p.append((int(lm.x * width), int(lm.y * height)))

    vertical1 = ((p[1][1]-p[5][1])**2 +
                 (p[1][0]-p[5][0])**2)**0.5
    vertical2 = ((p[2][1]-p[4][1])**2 +
                 (p[2][0]-p[4][0])**2)**0.5
    horizontal = ((p[0][1]-p[3][1])**2 +
                  (p[0][0]-p[3][0])**2)**0.5

    return (vertical1 + vertical2) / (2 * horizontal) if horizontal else 0

camera = cv2.VideoCapture(0)
closed_since = None
last_command = ""
last_send = 0

with FaceLandmarker.create_from_options(options) as landmarker:
    while camera.isOpened():
        success, frame = camera.read()
        if not success:
            break

        height, width = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = landmarker.detect(mp_image)
        command = "NOFACE"

        if result.face_landmarks:
            points = result.face_landmarks[0]

            left = eye_ratio(points, LEFT_EYE, width, height)
            right = eye_ratio(points, RIGHT_EYE, width, height)
            ratio = (left + right) / 2

            if ratio < 0.20:
                if closed_since is None:
                    closed_since = time.time()

                if time.time() - closed_since >= 2:
                    command = "DROWSY"
                else:
                    command = "AWAKE"
            else:
                closed_since = None
                command = "AWAKE"

        if command != last_command and time.time() - last_send > 0.5:
            arduino.write((command + "\n").encode())
            last_command = command
            last_send = time.time()

        cv2.putText(frame, command, (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255) if command == "DROWSY"
                    else (0, 255, 0), 2)

        cv2.imshow("EV Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
arduino.close()