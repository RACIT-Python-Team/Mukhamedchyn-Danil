import cv2
import numpy as np

lower_color = np.array([100, 150, 20])
upper_color = np.array([130, 255, 150])

video = cv2.VideoCapture(r'C:\Users\danam\PycharmProjects\Mukhamedchyn-Danil\Block3\video\0001-0100.mkv')
while True:
    ret, frame = video.read()
    if not ret:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Origframe', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Filtered Result', result)



    if cv2.waitKey(70) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
