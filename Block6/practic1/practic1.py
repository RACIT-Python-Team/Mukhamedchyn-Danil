import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
my_hands = mp_hands.Hands(static_image_mode = False,
                          max_num_hands=2,
                          )
INTERACTIVE_ZONE = [
    {"name": "Reception Area", "norm_coords": [0.10, 0.10, 0.45, 0.40], "color": (255, 255, 0)},
    {"name": "Room 1 (Staff)", "norm_coords": [0.55, 0.10, 0.90, 0.40], "color": (0, 0, 255)},
    {"name": "Emergency Exit", "norm_coords": [0.30, 0.60, 0.70, 0.90], "color": (0, 0, 255)}
]

def create_virtual_map(W, H):
    map_img = np.zeros((H, W, 3), dtype=np.uint8)
    for i in range(10):
        # По X
        cv2.line(map_img,(0, int(H * i / 10)),(W, int(H * i / 10)),(255, 0, 0),1)
        # По Y
        cv2.line(map_img,(int(W * i / 10), 0),(int(W * i / 10), H),(255, 0, 0),1)

    cv2.putText(map_img, "Virtual Map", (W//2-100, H-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return map_img

video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape
    ROI_W = int(W*0.7)
    ROI_H = int(H*0.8)
    ROI_W_START = int((W-ROI_W)/2)
    ROI_H_START = int((H-ROI_H)/2)
    TOUCH_Y_ABS = int(H*0.55)
    virtual_map = create_virtual_map(ROI_W, ROI_H)
    for zone in INTERACTIVE_ZONE:
        min_x_pixel = int(zone["norm_coords"][0]*ROI_W)
        min_y_pixel = int(zone["norm_coords"][1]*ROI_H)
        max_x_pixel = int(zone["norm_coords"][2]*ROI_W)
        max_y_pixel = int(zone["norm_coords"][3]*ROI_H)
        cv2.rectangle(virtual_map, (min_x_pixel, min_y_pixel), (max_x_pixel, max_y_pixel), zone["color"], -1)
        cv2.putText(virtual_map, zone["name"], (min_x_pixel+10, min_y_pixel+30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    frame[ROI_H_START : ROI_H_START + ROI_H,
    ROI_W_START : ROI_W_START + ROI_W] = virtual_map
    cv2.line(frame, (0, TOUCH_Y_ABS), (W, TOUCH_Y_ABS), (255, 0, 0), 1)
    cv2.putText(frame, "Y-AXIS TOUCH THRESHOLD", (10, TOUCH_Y_ABS - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = my_hands.process(frame_rgb)
    if results.multi_hand_landmarks is not None:
        for hand_landmark in results.multi_hand_landmarks:
            abs_x = int(hand_landmark.landmark[8].x*W)
            abs_y = int(hand_landmark.landmark[8].y*H)
            is_touching_y = abs_y <TOUCH_Y_ABS
            is_in_roi = (abs_x >ROI_W_START and abs_x <ROI_W_START + ROI_W
            and abs_y >ROI_H_START and abs_y <ROI_H_START + ROI_H)
            finger_color = (0, 255, 0)
            if is_touching_y and is_in_roi:
                relative_x = abs_x-ROI_W_START
                relative_y = abs_y-ROI_H_START
                scalar_x = relative_x/ROI_W
                scalar_y = relative_y/ROI_H
                finger_color = (255, 255, 0)
                detected_zone = None
                for zone in INTERACTIVE_ZONE:
                    min_x, min_y, max_x, max_y = zone["norm_coords"]
                    if(scalar_x>=min_x and scalar_x<=max_x and scalar_y>=min_y and scalar_y<=max_y):
                        detected_zone = zone
                        finger_color = zone["color"]
                        break
                if detected_zone:
                    status_text = f"Detected zone: {detected_zone}"
                    print(f"!!!TOUCH DETECTED : {detected_zone} at ({scalar_x:.2f},{scalar_y:.2f})")
                else:
                    status_text = f"ACTIVE: Unmapped Area"
                cv2.putText(frame, status_text, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, finger_color, 2)
                cv2.putText(frame, f"N-Coords: ({scalar_x:.2f}, {scalar_y:.2f})", (5, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, finger_color, 2)

            else:
                status_text = "READY / OUTSIDE ZONE"
                cv2.putText(frame, status_text, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            cv2.circle(frame, (abs_x, abs_y), 5, finger_color, -1)
    cv2.imshow('Interactive Map Detection', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
my_hands.close()
video.release()
cv2.destroyAllWindows()
