from tkinter import messagebox
import cv2
import numpy as np
import mediapipe as mp




def hands_tracking():

    print("test")
    mp_hands = mp.solutions.hands
    my_hands = mp_hands.Hands(static_image_mode=False,
                              max_num_hands=2,
                              min_detection_confidence=0.5,
                              min_tracking_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        video.release()
        return messagebox.showerror("Error", "Error in connected cameras")

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            raise ValueError ("Loss of connection with the camera")
            break
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = my_hands.process(frame_rgb)
        if results.multi_hand_landmarks is not None:
            for hand_landmark in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame,
                                          hand_landmark,
                                          mp_hands.HAND_CONNECTIONS)
            count = len(results.multi_hand_landmarks)
            cv2.putText(frame,
                        f"Found hands: {count}",
                        (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2)
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
    my_hands.close()

lower_color = np.array([0, 0, 0])
upper_color = np.array([0, 0, 0])

def tracking_object(event):
    mp_drawing = mp.solutions.drawing_utils
    def tracking(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            global lower_color, upper_color
            hsv_value = hsv_frame[y, x]
            h_value = hsv_value[0]
            s_value = hsv_value[1]
            v_value = hsv_value[2]
            lower_color = np.array([max(0, h_value-10), max(0, s_value-10), max(0, v_value-10)])
            upper_color = np.array([min(255,h_value+10), min(255, s_value+10), min(255, v_value+10)])

    cv2.namedWindow("Tracking object")
    cv2.setMouseCallback("Tracking object", tracking)
    video = cv2.VideoCapture(r'C:\Users\danam\PycharmProjects\Mukhamedchyn-Danil\Block3\video\0001-0100.mkv')
    if not video.isOpened():
        return messagebox.showerror("Error", "Video capture failed")
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)
            cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
        cv2.imshow("Tracking object", frame)
        if cv2.waitKey(70) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()




