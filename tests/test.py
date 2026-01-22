import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
my_hands = mp_hands.Hands(static_image_mode=False,
                          max_num_hands=1,
                          min_detection_confidence=0.5,
                          min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

img_canvas = None
xp, yp = 0, 0
draw_color = (255, 0, 255)

brush_thickness = 10

video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    H, W, Z = frame.shape

    if img_canvas is None:
        img_canvas = np.zeros((H, W, 3), dtype=np.uint8)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = my_hands.process(frame_rgb)

    if results.multi_hand_landmarks is not None:
        for hand_landmark in results.multi_hand_landmarks:
            x = int(hand_landmark.landmark[8].x*W)
            y = int(hand_landmark.landmark[8].y*H)
            if xp == 0 and yp == 0:
                xp, yp = x, y
            cv2.line(img_canvas, (xp, yp), (x, y), draw_color, brush_thickness)
            # оновлюємо змінні
            xp, yp = x, y
    else:
        xp, yp = 0, 0

    img_gray = cv2.cvtColor(img_canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)

    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, img_inv)
    frame = cv2.bitwise_or(frame, img_canvas)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('c'):
        img_canvas = np.zeros((H, W, 3), dtype=np.uint8)  # Очищаємо полотно

video.release()
cv2.destroyAllWindows()
my_hands.close()