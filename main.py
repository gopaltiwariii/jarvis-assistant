from jarvis.audio import speak, listen
from jarvis.brain import process_command

def run_jarvis():
    """Main loop for the Jarvis assistant."""
    speak("Initializing Jarvis systems.")
    speak("All systems are online. How can I help you today?")
    
    while True:
        try:
            query = listen()
            
            if query == "none" or query == "":
                continue
                
            response = process_command(query)
            speak(response)
            
            if "goodbye" in response.lower():
                break
                
        except KeyboardInterrupt:
            speak("Emergency shut down initiated. Goodbye.")
            break

if __name__ == "__main__":
    run_jarvis()
