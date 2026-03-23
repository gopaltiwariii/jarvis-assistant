import subprocess
import speech_recognition as sr

import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import os

def speak(text):
    """Speaks the given text out loud."""
    print(f"Jarvis: {text}")
    
    # Escape single quotes for PowerShell command
    safe_text = text.replace("'", "''")
    # Using PowerShell's built in Speech module (native to Windows, requires no pip install)
    ps_script = f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{safe_text}')"
    cmd = ["powershell", "-Command", ps_script]
    
    # Run synchronously. CREATE_NO_WINDOW prevents flashing cmd boxes if launched outside of a console
    creationflags = getattr(subprocess, 'CREATE_NO_WINDOW', 0x08000000) if os.name == 'nt' else 0
    subprocess.run(cmd, creationflags=creationflags)

def listen():
    """Listens to the microphone and returns the recognized text."""
    recognizer = sr.Recognizer()
    fs = 44100
    duration = 5  # seconds
    
    print("Listening... (Speak for up to 5 seconds)")
    try:
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        
        # Save as temp file
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, "jarvis_temp_audio.wav")
        wav.write(temp_path, fs, myrecording)
        
        with sr.AudioFile(temp_path) as source:
            # We skip ambient noise adjustment here as it might clip short recordings
            audio = recognizer.record(source)
            
        # Clean up
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
    except Exception as e:
        print(f"Audio recording error: {e}")
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
