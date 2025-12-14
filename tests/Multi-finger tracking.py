import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
MyHands = mp_hands.Hands(static_image_mode=False,
                         max_num_hands=1,
                         min_detection_confidence=0.5,
                         min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = MyHands.process(frame_rgb)
    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,
                                   hand_landmarks,
                                   mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((0,0, 255), 2, 5),
                                   mp_draw.DrawingSpec((0,255, 0), 2, 2),)
            thumb=hand_landmarks.landmark[4]
            Tx=int(thumb.x*W)
            Ty=int(thumb.y*H)
            cv2.circle(frame, (Tx, Ty), 5, (0,0,255), -1 )

            index=hand_landmarks.landmark[8]
            Ix=int(index.x*W)
            Iy=int(index.y*H)
            cv2.circle(frame, (Ix, Iy), 5, (0,0,255), -1)

            pinky=hand_landmarks.landmark[20]
            Px=int(pinky.x * W)
            Py=int(pinky.y * H)
            cv2.circle(frame, (Px, Py), 5, (0,0,255), -1)


    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
MyHands.close()
video.release()
cv2.destroyAllWindows()