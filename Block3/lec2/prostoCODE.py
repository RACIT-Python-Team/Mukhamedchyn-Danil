import cv2
import numpy as np

lower_color = np.array([100, 150, 20])
upper_color = np.array([130, 255, 150])

video = cv2.VideoCapture(r'C:\Users\danam\PycharmProjects\Mukhamedchyn-Danil\Block3\video\0001-0100.mkv')
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    hsv_color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_color, lower_color, upper_color)
    contour, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contour) > 0:
        largest_contour = max(contour, key=cv2.contourArea)
        if cv2.contourArea(largest_contour)>500:
            M = cv2.moments(largest_contour)
            if M['m00']!=0:
                cX = int(M['m10']/M['m00'])
                cY = int(M['m01']/M['m00'])
                cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)
                cv2.putText(frame, (f"x: {cX}, y: {cY}"), (cX - 10, cY + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()