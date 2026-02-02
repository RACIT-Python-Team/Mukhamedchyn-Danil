from Block7 import voice_engine
from hand_tracker import HandTracker
import cv2
import map_engine

video = cv2.VideoCapture(0)
last_zone = None
finger_tracker = HandTracker()
plan_img = cv2.imread("plan.png")
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    finger_pos = finger_tracker.handTracker(frame)
    H, W, _ = frame.shape
    plan_display = cv2.resize(plan_img, (W, H))
    current_zone = None
    if finger_pos:
        x, y = finger_pos
        cv2.circle(plan_display, (x, y), 10, (0, 0, 255), -1)
        map_engine.active_zone(x, y)
        current_zone = map_engine.active_zone(x, y)
    if current_zone is not None:
        if current_zone != last_zone:
            voice_engine.speak(current_zone)
            last_zone = current_zone
    else:
        last_zone = None
    cv2.imshow("Smart Kiosk", plan_display)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
