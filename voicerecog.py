import speech_recognition as sr
from gpiozero import LED
from time import sleep

# Setup GPIO
led = LED(17)  

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
mic = sr.Microphone()

# Function to recognize speech and control LED
def listen_and_control():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        print("Listening...")

        while True:
            try:
                # Listen for audio 
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower()  # Convert to lowercase for easier comparison
                print(f"You said: {text}")

                # Control the LED based on the voice command
                if "turn on the light" in text:
                    led.on()  # Turn on the LED
                    print("Light turned ON")
                elif "turn off the light" in text:
                    led.off()  # Turn off the LED
                    print("Light turned OFF")
                else:
                    print("Unknown command. Please say 'turn on the light' or 'turn off the light'.")

            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
            except sr.RequestError as e:
                print(f"Error connecting to Google Speech Recognition service; {e}")

# Main function to run the program
def main():
    try:
        listen_and_control()  # Start listening and controlling the LED
    except KeyboardInterrupt:
        print("Program stopped.")

if _name_ == "_main_":
    main()
