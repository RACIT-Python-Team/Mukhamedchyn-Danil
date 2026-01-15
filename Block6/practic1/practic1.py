import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7)

INTERACTIVE_ZONES = [
    {"name": "Reception", "norm_coords": [0.1, 0.1, 0.45, 0.4], "color": (255, 255, 0)},
    {"name": "Staff Room", "norm_coords": [0.55, 0.1, 0.9, 0.4], "color": (0, 165, 255)},
    {"name": "Exit", "norm_coords": [0.3, 0.6, 0.7, 0.9], "color": (0, 0, 255)}
]

def create_virtual_map(W, H):
    map_img = np.zeros((H, W, 3), dtype=np.uint8)
    cv2.rectangle(map_img, (0, 0), (W, H), (20, 20, 20), -1)  # Темно-сірий фон
    cv2.putText(map_img, "VIRTUAL MAP", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return map_img

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape

    ROI_W = int(W * 0.7)
    ROI_H = int(H * 0.8)
    ROI_X_START = int((W - ROI_W) / 2)
    ROI_Y_START = int((H - ROI_H) / 2)
    TOUCH_THRESHOLD = int(H * 0.55)

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    virtual_map = create_virtual_map(ROI_W, ROI_H)

    for zone in INTERACTIVE_ZONES:
        x1 = int(zone["norm_coords"][0] * ROI_W)
        y1 = int(zone["norm_coords"][1] * ROI_H)
        x2 = int(zone["norm_coords"][2] * ROI_W)
        y2 = int(zone["norm_coords"][3] * ROI_H)
        cv2.rectangle(virtual_map, (x1, y1), (x2, y2), zone["color"], -1)
        cv2.putText(virtual_map, zone["name"], (x1, y1 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    frame[ROI_Y_START: ROI_Y_START + ROI_H, ROI_X_START: ROI_X_START + ROI_W] = virtual_map

    cv2.line(frame, (0, TOUCH_THRESHOLD), (W, TOUCH_THRESHOLD), (0, 255, 255), 2)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            tip = hand_landmarks.landmark[8]
            abs_x = int(tip.x * W)
            abs_y = int(tip.y * H)

            is_touching = abs_y < TOUCH_THRESHOLD
            in_roi = (ROI_X_START < abs_x < ROI_X_START + ROI_W) and (ROI_Y_START < abs_y < ROI_Y_START + ROI_H)

            color = (0, 255, 0)

            if is_touching and in_roi:
                color = (0, 255, 255)
                rel_x = (abs_x - ROI_X_START) / ROI_W
                rel_y = (abs_y - ROI_Y_START) / ROI_H

                for zone in INTERACTIVE_ZONES:
                    zx1, zy1, zx2, zy2 = zone["norm_coords"]
                    if zx1 <= rel_x <= zx2 and zy1 <= rel_y <= zy2:
                        color = zone["color"]
                        cv2.putText(frame, f"CLICK: {zone['name']}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            cv2.circle(frame, (abs_x, abs_y), 10, color, -1)

    cv2.imshow('Touch Interface', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()