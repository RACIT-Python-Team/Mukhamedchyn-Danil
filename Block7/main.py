from Block7 import voice_engine
from hand_tracker import HandTracker
import cv2
import map_engine

video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)

finger_tracker = HandTracker()
plan_img_original = cv2.imread("plan.png")

last_announced_zone = None

print("Система запущена. Натисни 'q' для виходу.")

while video.isOpened():
    ret, frame = video.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape
    plan_display = cv2.resize(plan_img_original, (W, H))
    finger_pos = finger_tracker.handTracker(frame)
    current_zone = None
    if finger_pos:
        x, y = finger_pos
        cv2.circle(plan_display, (x, y), 15, (255, 0, 0), -1)
        current_zone = map_engine.active_zone(x, y)

    if current_zone:
        cv2.putText(plan_display, current_zone, (x + 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if current_zone != last_announced_zone:
            print(f"Зміна зони: {current_zone}")
            voice_engine.speak(current_zone)
            last_announced_zone = current_zone

    else:
        last_announced_zone = None

    cv2.imshow("Smart Kiosk", plan_display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()