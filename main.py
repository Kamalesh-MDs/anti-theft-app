import cv2

cam = cv2.VideoCapture(0)
ret, frame = cam.read()

if ret:
    cv2.imwrite("Proof.jpg",frame)
    print("Image saved.")
else:
    print("Failed to capture image." )
cam.release()