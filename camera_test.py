import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera could not be opened.")
    exit()

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read camera.")
        break

    cv2.imshow("EV Driver Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()