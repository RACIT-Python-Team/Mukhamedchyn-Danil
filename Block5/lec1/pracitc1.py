import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode = False,
                       max_num_hands = 1,
                       min_detection_confidence = 0.5,
                       min_tracking_confidence = 0.5)
mp_drawing = mp.solutions.drawing_utils

video = cv2.VideoCapture(0)
is_touching = False

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    frame = cv2.flip(frame,1) # присвоїли
    h, w, _ = frame.shape
    TOUCH_THRESHOLD_Y = int(h*0.6)#задаємо координати для лінії на 60% екрану
    cv2.line(frame, (0, TOUCH_THRESHOLD_Y), (w, TOUCH_THRESHOLD_Y), (0, 255, 0), 2)
    cv2.putText(frame, "YOUCH SURFACE(Y = 60%)", (10, TOUCH_THRESHOLD_Y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            pixel_x = int(hand_landmarks.landmark[8].x*w)
            pixel_y = int(hand_landmarks.landmark[8].y*h)
            cv2.circle(frame, (pixel_x, pixel_y), 5, (0, 0, 255), -1)
            if pixel_y > TOUCH_THRESHOLD_Y:
                is_touching = True
                touch_status = "TOUCHING"
                color = (0, 0, 255)
            else:
                is_touching = False
                touch_status = "NOT TOUCHING"
                color = (0, 255, 0)
            cv2.putText(frame, touch_status, (pixel_x+20, pixel_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
            cv2.circle(frame, (pixel_x, pixel_y), 15, color, 2)
    cv2.imshow("'Touch Detection by Y-Coordinate'", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
hands.close()
video.release()
cv2.destroyAllWindows()