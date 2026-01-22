import cv2
import numpy as np

frame = None

cap = cv2.VideoCapture(r'C:\Users\danam\PycharmProjects\Mukhamedchyn-Danil\Block3\video\0001-0100.mkv')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_color = np.array([100, 150, 20])
    upper_color = np.array([130, 255, 150])

    mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
            cv2.circle(frame, (cX, cY), 7, (0, 0, 255), -1)
            text = f"X: {cX}, Y: {cY}"
            cv2.putText(frame, f"Center: ({cX}, {cY})", (cX + 10, cY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow('Object Tracking', frame)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()