import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
MyHands = mp_hands.Hands(static_image_mode = False,
                         max_num_hands = 2,
                         min_detection_confidence = 0.5,
                         min_tracking_confidence = 0.5)
mp_draw = mp.solutions.drawing_utils

video = cv2.VideoCapture(r'C:\Users\danam\PycharmProjects\Mukhamedchyn-Danil\Block2\video\video_2025-12-13_14-39-35.mp4')
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = MyHands.process(frame_rgb)
    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
MyHands.close()
cv2.destroyAllWindows()
video.release()