import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
my_hands = mp_hands.Hands(max_num_hands=1,
                          min_detection_confidence=0.5,
                          min_tracking_confidence=0.5,
                          static_image_mode=False)
mp_drawing = mp.solutions.drawing_utils
ROI_W = 400
ROI_H = 400
video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    W, H, _ = frame.shape
    ROI_X_START = (W-ROI_W)/2
    ROI_Y_START = (H-ROI_H)/2
    cv2.rectangle(frame, (ROI_X_START, ROI_Y_START), (ROI_X_START+ROI_W, ROI_Y_START+ROI_H), (0,255,0), 3)
    cv2.putText(frame, "Virtual Camera", (ROI_X_START, ROI_Y_START-10), (0,0,255), 2)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = my_hands.process(frame_rgb)
    if results.multi_hand_landmarks is not None:
        for hand_landmark in results.multi_hand_landmark:
            pixel_x = int(hand_landmark.landmark[8]*W)
            pixel_y = int(hand_landmark.landmark[8]*H)
            if (pixel_x>ROI_X_START and pixel_y < ROI_Y_START and
                pixel_x < ROI_X_START+ROI_W and pixel_y < ROI_Y_START+ROI_H):
                x = pixel_x-ROI_X_START
                y = pixel_y-ROI_Y_START
                scalar_x = x/ROI_W
                scalar_y = y/ROI_H
                cv2.circle(frame, (x, y), 5, (0,0,255), -1)