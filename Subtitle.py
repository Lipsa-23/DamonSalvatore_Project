import speech_recognition as sr
import sys

def real_time_subtitles():
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source)
            print("Microphone is ready. Start speaking...")

            while True:
                try:
                    print("\nListening...")
                    audio = recognizer.listen(source, timeout=5)  # Timeout if no speech
                    text = recognizer.recognize_google(audio)
                    print(f"Transcript: {text}")
                except sr.UnknownValueError:
                    print("I couldn't understand. Please speak again.")
                except sr.WaitTimeoutError:
                    print("Listening timed out. No speech detected.")
                except sr.RequestError as e:
                    print(f"API error: {e}")
                    sys.exit(1)
    except OSError as e:
        print(f"Microphone error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProgram terminated. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    real_time_subtitles()