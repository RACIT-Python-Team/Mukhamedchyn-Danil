import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1)

INTERACTIVE_ZONES = [
    {
        "name": "Reception Area",
        "norm_coords": [0.10, 0.10, 0.45, 0.40],
        "color": (255, 255, 0)  # Yellow
    },
    {
        "name": "Room 1 (Staff)",
        "norm_coords": [0.55, 0.10, 0.90, 0.40],
        "color": (0, 165, 255)  # Orange
    },
    {
        "name": "Emergency Exit",
        "norm_coords": [0.30, 0.60, 0.70, 0.90],
        "color": (0, 0, 255)
    }
    ]

def create_virtual_map(W, H, zones):
    virtual_map = np.zeros((H, W, 3), dtype = np.uint8)
    for zone in zones:
        x1 = int(zone["norm_coords"][0]*W)
        y1 = int(zone["norm_coords"][1]*H)
        x2 = int(zone["norm_coords"][2]*W)
        y2 = int(zone["norm_coords"][3]*H)
        zone["pixel_coords"] = (x1, y1, x2, y2)

        cv2.rectangle(virtual_map, (x1, y1), (x2, y2), zone["color"], -1)
        cv2.putText(virtual_map, zone["name"], (x1, y1-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, zone["color"], 2)
    return virtual_map

video = cv2.VideoCapture(0)
while video.isOpened():
    color = (0, 255, 0)
    ret, frame = video.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    Y, X, _ = frame_rgb.shape
    ROI_X = int(X*0.7)
    ROI_Y = int(Y*0.7)
    ROI_X_START = int((X-ROI_X)/2)
    ROI_Y_START = int((Y-ROI_Y)/2)
    results = hands.process(frame_rgb)
    virtual_map = create_virtual_map(ROI_X, ROI_Y, INTERACTIVE_ZONES)
    frame[ROI_Y_START:ROI_Y_START+ROI_Y, ROI_X_START:ROI_X_START+ROI_X] = virtual_map

    if results.multi_hand_landmarks is not None:
        for hand_landmark in results.multi_hand_landmarks:
            abs_x = int(hand_landmark.landmark[8].x*X)
            abs_y = int(hand_landmark.landmark[8].y*Y)
            in_roi = (abs_x>ROI_X_START and abs_x<ROI_X_START+ROI_X and abs_y>ROI_Y_START and abs_y<ROI_Y_START+ROI_Y)
            if in_roi:
                norm_x = (abs_x - ROI_X_START)/ROI_X
                norm_y = (abs_y - ROI_Y_START)/ROI_Y
                for zone in INTERACTIVE_ZONES:
                    zx1, zy1, zx2, zy2 = zone["norm_coords"]
                    if (norm_x>zx1 and norm_x<zx2 and norm_y>zy1 and norm_y<zy2):
                        color = zone["color"]
                        cx1, cy1, cx2, cy2 = zone["pixel_coords"]
                        cv2.putText(virtual_map, zone["name"], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, zone["color"], 2)
                        cv2.rectangle(virtual_map, (cx1, cy1), (cx2, cy2), (255, 255, 255), 4)
            cv2.circle(frame, (abs_x, abs_y), 1, color, 3)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
hands.close()