import cv2
import mediapipe as mp

myhand = mp.solutions.hands # підключаємо модуль hands
hands = myhand.Hands(static_image_mode=False,
max_num_hands=2,
min_detection_confidence=0.5,
min_tracking_confidence=0.5
                     ) # об'єкт на основі класу
mp_draw = mp.solutions.drawing_utils # підключаємо малювання

video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    if not ret:
        break
    frame=cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)#конвертація кольору для mp
    results = hands.process(frame_rgb)# записуємо список .multi_hand_landmarks у result

    countHands = 0

    if results.multi_hand_landmarks is not None: # перевіряємо чи пустий список

        countHands = len(results.multi_hand_landmarks)# рахуємо кількість рук

        for hand_landmarks in results.multi_hand_landmarks: # перебираємо кожен об'єкт(руку) зі списку
            mp_draw.draw_landmarks(frame,
                                   hand_landmarks,
                                   myhand.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec(color=(255, 0, 0), circle_radius=5),
                                   mp_draw.DrawingSpec(color=(0, 255, 0))
                                   )

            h, w, c = frame.shape

            point_8 = hand_landmarks.landmark[8]

            x, y = int(point_8.x * w), int(point_8.y * h)

            print(f"Index Finger: x={x}, y={y}")

            cv2.circle(frame, (x, y), 15, (255, 0, 255), cv2.FILLED)

    cv2.putText(frame,
                f"Hands: {countHands}",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color=(0, 255, 0),
                thickness=2) # добавляємо кількість рук на екран
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()