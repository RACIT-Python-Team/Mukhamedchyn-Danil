import cv2

myVideo=cv2.VideoCapture(0)
while True:
    ret, frame = myVideo.read()
    if not ret:
        break
    cv2.imshow('Camera',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
myVideo.release()
cv2.destroyAllWindows()