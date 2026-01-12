#Відстеження об'єкта, який був вибраний лівою кнопкою миші під час запису відео екрана/камери

import cv2
import numpy as np

lower_color = np.array([0, 0, 0])
upper_color = np.array([0, 0, 0])

def color_picker(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global lower_color, upper_color
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_value = hsv_frame[y, x]

        h_value = hsv_value[0]
        s_value = hsv_value[1]
        v_value = hsv_value[2]

        lower_color = np.array([max(0, h_value-10), max(0, s_value-40), max(0, v_value-40) ])
        upper_color = np.array([min(179, h_value+10), min(255, s_value+40), min(255, v_value+40) ])


cv2.namedWindow("test")
cv2.setMouseCallback("test", color_picker)
video = cv2.VideoCapture(r'C:\Users\danam\PycharmProjects\Mukhamedchyn-Danil\Block3\video\0001-0100.mkv')
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    hsv_value = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_value, lower_color, upper_color)
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
    cv2.imshow("test", frame)
    if cv2.waitKey(70) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()