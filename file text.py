import speech_recognition as sr

def listen_and_write(filename="output.txt"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening... Press Ctrl+C to stop.")

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            with open(filename, "a") as f:
                while True:
                    print("Speak:")
                    audio = recognizer.listen(source)

                    try:
                        text = recognizer.recognize_google(audio)
                        print("You said:", text)
                        f.write(text + "\n")
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                    except sr.RequestError as e:
                        print(f"API error: {e}")

    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    listen_and_write()
