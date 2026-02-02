import pyttsx3
import threading

# Створюємо "замок". Це як табличка "Зайнято" на туалеті.
# Поки один потік там, інший не зайде.
voice_lock = threading.Lock()


def _speak_thread(text):
    """
    Ця функція виконується в окремому потоці.
    """
    # Заходимо в захищений блок.
    # (Насправді, ми вже перевірили замок в speak, але це подвійний захист)
    with voice_lock:
        try:
            # Ініціалізуємо двигун З НУЛЯ
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)

            # Говоримо
            engine.say(text)
            engine.runAndWait()

            # Вбиваємо двигун, щоб очистити пам'ять
            engine.stop()
            del engine
        except Exception as e:
            print(f"Помилка голосу: {e}")


def speak(text):
    """
    Головна функція.
    """
    # 1. Перевіряємо, чи вільний "рот" комп'ютера.
    # Якщо voice_lock.locked() == True, значить комп'ютер ще говорить.
    # Ми просто виходимо (return) і НЕ створюємо новий потік.
    if voice_lock.locked():
        # print(f"Skipped '{text}' because busy") # Можна розкоментувати для налагодження
        return

    # 2. Якщо вільно - запускаємо потік
    t = threading.Thread(target=_speak_thread, args=(text,))
    t.start()