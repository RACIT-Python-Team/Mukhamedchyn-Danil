import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
MyHands = mp_hands.Hands(static_image_mode=False,
                         max_num_hands=2,
                         min_detection_confidence=0.5,
                         min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

video=cv2.VideoCapture(0)
INDEX_FINGER_TIP_ID = 8
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape # прив'язуємо координати
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = MyHands.process(frame_rgb)
    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            tip = hand_landmarks.landmark[INDEX_FINGER_TIP_ID]
            pixel_x = int(tip.x*W)
            pixel_y = int(tip.y*H)
            cv2.circle(frame, (pixel_x, pixel_y), 15, (0,0,255), -1)
            text = f"X: {pixel_x}, Y: {pixel_y}"
            cv2.putText(frame,
                        text,
                        (pixel_x, pixel_y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0,0,255),
                        2)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
MyHands.close()
video.release()
cv2.destroyAllWindows()