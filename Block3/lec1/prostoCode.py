import cv2
import numpy as np

def get_hsv_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_value = hsv_frame[y, x]
        print(f"BGR: {frame[y, x]}")
        print(f"HSV: {hsv_value}")
        print('-'*30)
frame = None
cv2.namedWindow('ColorPicker')
cv2.setMouseCallback('ColorPicker', get_hsv_color)
video = cv2.VideoCapture(r'C:\Users\danam\PycharmProjects\Mukhamedchyn-Danil\Block3\video\0001-0100.mkv')
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow('ColorPicker', frame)
    if cv2.waitKey(0) & 0xFF == ord('y'):
        break
video.release()
cv2.destroyAllWindows()