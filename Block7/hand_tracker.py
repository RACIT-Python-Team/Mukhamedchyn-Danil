import cv2
import mediapipe as mp
class HandTracker:

    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                max_num_hands=1)

    def handTracker(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        Y, X, _ = frame.shape
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                FINGER = hand_landmarks.landmark[8]
                fx = int(FINGER.x*X)
                fy = int(FINGER.y*Y)
                return fx, fy
            return None