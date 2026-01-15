import cv2
import mediapipe as mp
import numpy as np

# Ініціалізація модулів MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5)

# --- 1. Конфігурація Інтерактивних Зон (Нормалізовані Координати) ---
# [min_x, min_y, max_x, max_y] від 0.0 до 1.0 на самому макеті
INTERACTIVE_ZONES = [
    {"name": "Reception Area", "norm_coords": [0.10, 0.10, 0.45, 0.40], "color": (255, 255, 0)},
    {"name": "Room 1 (Staff)", "norm_coords": [0.55, 0.10, 0.90, 0.40], "color": (0, 165, 255)},
    {"name": "Emergency Exit", "norm_coords": [0.30, 0.60, 0.70, 0.90], "color": (0, 0, 255)}
]
INDEX_FINGER_TIP_ID = 8


# --- 2. Функція для створення віртуального макета (заглушка) ---
def create_virtual_map(W, H):
    # Створюємо простий чорний макет для демонстрації
    map_img = np.zeros((H, W, 3), dtype=np.uint8)
    # Додаємо сітку для візуалізації
    for i in range(1, 10):
        # Горизонтальні лінії
        cv2.line(map_img, (0, int(H * i / 10)), (W, int(H * i / 10)), (50, 50, 50), 1)
        # Вертикальні лінії
        cv2.line(map_img, (int(W * i / 10), 0), (int(W * i / 10), H), (50, 50, 50), 1)

    cv2.putText(map_img, "VIRTUAL MAP", (W // 2 - 100, H - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    return map_img


# --- 3. Основний цикл обробки ---
cap = cv2.VideoCapture(0)

# Глобальні налаштування ROI
ROI_WIDTH_PERCENT = 0.7
ROI_HEIGHT_PERCENT = 0.8
TOUCH_THRESHOLD_Y_PERCENT = 0.55  # Поріг "дотику" (вище 55% висоти кадру)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape

    # Обчислення піксельних меж ROI
    ROI_W = int(W * ROI_WIDTH_PERCENT)
    ROI_H = int(H * ROI_HEIGHT_PERCENT)
    ROI_X_START = int((W - ROI_W) / 2)
    ROI_Y_START = int((H - ROI_H) / 2)

    # Визначення порогу "дотику" (по відношенню до всього кадру)
    TOUCH_THRESHOLD_Y_ABS = int(H * TOUCH_THRESHOLD_Y_PERCENT)

    # --- 4. Накладання Макета ---
    virtual_map = create_virtual_map(ROI_W, ROI_H)

    # Малюємо всі зони на самому макеті
    for zone in INTERACTIVE_ZONES:
        min_x_pix = int(zone["norm_coords"][0] * ROI_W)
        min_y_pix = int(zone["norm_coords"][1] * ROI_H)
        max_x_pix = int(zone["norm_coords"][2] * ROI_W)
        max_y_pix = int(zone["norm_coords"][3] * ROI_H)

        # Малюємо прямокутник на віртуальному макеті
        cv2.rectangle(virtual_map,
                      (min_x_pix, min_y_pix),
                      (max_x_pix, max_y_pix),
                      zone["color"],
                      -1)  # -1 для заповнення
        # Додаємо назву зони
        cv2.putText(virtual_map, zone["name"], (min_x_pix + 10, min_y_pix + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    # Вставляємо віртуальний макет у кадр (область ROI)
    frame[ROI_Y_START: ROI_Y_START + ROI_H,
    ROI_X_START: ROI_X_START + ROI_W] = virtual_map

    # Малюємо лінію порогу "дотику" для візуального контролю
    cv2.line(frame, (0, TOUCH_THRESHOLD_Y_ABS), (W, TOUCH_THRESHOLD_Y_ABS), (0, 255, 255), 2)
    cv2.putText(frame, "Y-AXIS TOUCH THRESHOLD", (10, TOUCH_THRESHOLD_Y_ABS - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (0, 255, 255), 2)

    # --- 5. Обробка Руки ---
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            tip = hand_landmarks.landmark[INDEX_FINGER_TIP_ID]

            # Піксельні координати кінчика пальця (всього кадру)
            abs_x = int(tip.x * W)
            abs_y = int(tip.y * H)

            # --- 6. Перевірка Умов та Масштабування ---

            # a) Умова "Дотику" (по Y-координаті)
            is_touching_y = abs_y < TOUCH_THRESHOLD_Y_ABS

            # b) Умова "Потрапляння в ROI"
            is_in_roi = (abs_x >= ROI_X_START and abs_x <= ROI_X_START + ROI_W and
                         abs_y >= ROI_Y_START and abs_y <= ROI_Y_START + ROI_H)

            # Малюємо палець
            finger_color = (0, 255, 0)

            if is_touching_y and is_in_roi:

                # Обчислюємо відносні координати всередині ROI (пікселі)
                relative_x = abs_x - ROI_X_START
                relative_y = abs_y - ROI_Y_START

                # Нормалізуємо відносні координати до 0.0-1.0 (для зіставлення з зонами)
                scaled_norm_x = relative_x / ROI_W
                scaled_norm_y = relative_y / ROI_H

                finger_color = (0, 255, 255)  # Жовтий, якщо умови виконані

                # --- 7. Зіставлення з Зонами (Point-in-Rectangle Test) ---

                detected_zone = None
                for zone in INTERACTIVE_ZONES:
                    min_x, min_y, max_x, max_y = zone["norm_coords"]

                    # Умова належності точки до прямокутника
                    if (scaled_norm_x >= min_x and scaled_norm_x <= max_x and
                            scaled_norm_y >= min_y and scaled_norm_y <= max_y):
                        detected_zone = zone["name"]
                        finger_color = zone["color"]  # Задаємо колір зони
                        break  # Знайшли збіг, виходимо з циклу перевірки зон

                # --- 8. Реакція на Зіставлення ---

                if detected_zone:
                    status_text = f"ACTIVE: {detected_zone}"
                    # Вивід у консоль
                    print(f"!!! TOUCH DETECTED: {detected_zone} at ({scaled_norm_x:.2f}, {scaled_norm_y:.2f})")
                else:
                    status_text = f"ACTIVE: Unmapped Area"

                # Візуалізація статусу
                cv2.putText(frame, status_text, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, finger_color, 2)
                cv2.putText(frame, f"N-Coords: ({scaled_norm_x:.2f}, {scaled_norm_y:.2f})", (5, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, finger_color, 2)

            else:
                # Палець не відповідає умовам (не в ROI або не "доторкається")
                status_text = "READY / OUTSIDE ZONE"
                cv2.putText(frame, status_text, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

            # Малюємо маркер пальця
            cv2.circle(frame, (abs_x, abs_y), 10, finger_color, -1)

    cv2.imshow('Interactive Map Detection', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

hands.close()
cap.release()
cv2.destroyAllWindows()
