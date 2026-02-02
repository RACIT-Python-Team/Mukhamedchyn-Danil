import pyttsx3
import threading

# Ініціалізація двигуна один раз при запуску
engine = pyttsx3.init()

def _speak_thread(text):
    """Ця функція працює у фоні"""
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass

def speak(text):
    """Цю функцію викликає main.py"""
    # Запускаємо голос в окремому потоці, щоб відео не гальмувало
    t = threading.Thread(target=_speak_thread, args=(text,))
    t.start()