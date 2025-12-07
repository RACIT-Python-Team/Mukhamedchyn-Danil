import cv2
import mediapipe as mp

myHands = mp.solutions.hands
hands = myHands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

circle = mp_draw.DrawingSpec(color=(0, 255, 255), circle_radius=5)
lines = mp_draw.DrawingSpec(color=(255,0,0), thickness=3)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks is not None:
        countHand = len(results.multi_hand_landmarks)

        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,
                                   hand_landmarks,
                                   myHands.HAND_CONNECTIONS,
                                   circle,
                                   lines)
    cv2.putText(frame_rgb,
                f"hands: {countHand}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow('Hands Detection',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()