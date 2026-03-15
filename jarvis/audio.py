import pyttsx3
import speech_recognition as sr

def initialize_engine():
    """Initializes the text-to-speech engine."""
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) # Index 0 for male, 1 for female usually
    return engine

engine = initialize_engine()

def speak(text):
    """Speaks the given text out loud."""
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to the microphone and returns the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return "None"

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you repeat?")
        return "None"
    except sr.RequestError:
        print("Sorry, my speech service is currently down.")
        return "None"
    except Exception as e:
        print(f"Error occurred: {e}")
        return "None"
    return query.lower()

if __name__ == "__main__":
    # Test the speaking capability
    speak("Hello sir, I am initializing my core systems. All systems are online.")
    # test listening
    speak("Sir, please say something to calibrate my microphone.")
    command = listen()
    speak(f"You said: {command}")
