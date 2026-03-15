from jarvis.audio import speak, listen
from jarvis.brain import process_command

def run_jarvis():
    """Main loop for the Jarvis assistant."""
    speak("Initializing Jarvis systems.")
    speak("All systems are online. How can I help you today?")
    
    # Normally we would use 'listen()' but due to a pyaudio 
    # installation issue on Python 3.14 we will use text input 
    # for the core testing, as we are still building the brain.
    # We can fix the audio input later!
    
    while True:
        try:
            # We'll use input() for now until pyAudio is fixed for Win/Python 3.14
            # query = listen()
            query = input("\nType a command (or type 'exit' to quit): ").lower()
            
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
