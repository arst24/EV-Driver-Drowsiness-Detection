import cv2
import mediapipe as mp
import math
import time

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="face_landmarker.task"),
    running_mode=RunningMode.IMAGE,
    num_faces=1
)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def distance(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def eye_ratio(points, eye):
    v1 = distance(points[eye[1]], points[eye[5]])
    v2 = distance(points[eye[2]], points[eye[4]])
    h = distance(points[eye[0]], points[eye[3]])
    return (v1 + v2) / (2 * h)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera could not be opened.")
    exit()

closed_start = None

with FaceLandmarker.create_from_options(options) as landmarker:

    while True:
        success, frame = camera.read()

        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = landmarker.detect(image)

        status = "NO FACE"

        if result.face_landmarks:

            points = result.face_landmarks[0]

            left = eye_ratio(points, LEFT_EYE)
            right = eye_ratio(points, RIGHT_EYE)

            ratio = (left + right) / 2

            if ratio < 0.20:

                if closed_start is None:
                    closed_start = time.time()

                closed_time = time.time() - closed_start

                if closed_time >= 2:
                    status = "DROWSY!"
                else:
                    status = "EYES CLOSED"

            else:
                closed_start = None
                status = "EYES OPEN"

        cv2.putText(
            frame,
            status,
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("EV Driver Drowsiness Detection", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()