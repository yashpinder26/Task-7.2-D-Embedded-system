import speech_recognition as sr  # Import the speech recognition library
from gpiozero import LED  # Import the GPIOZero library to control the LED
from time import sleep  # Import sleep for potential pauses if needed in the future

# Setup GPIO for the LED
led = LED(17)  # Define LED on GPIO pin 17

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio input source
mic = sr.Microphone()

# Function to recognize speech commands and control the LED based on voice input
def listen_and_control():
    with mic as source:  # Open the microphone resource
        # Adjust the recognizer to ambient noise levels for more accurate results
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for commands...")

        while True:
            try:
                # Listen to audio from the microphone
                audio = recognizer.listen(source)

                # Recognize speech using Google’s online speech recognition service
                text = recognizer.recognize_google(audio).lower()  # Convert recognized text to lowercase
                print(f"You said: {text}")

                # Check the recognized text for specific commands and control the LED
                if "turn on the light" in text:
                    led.on()  # Turn on the LED if command is recognized
                    print("Light turned ON")
                elif "turn off the light" in text:
                    led.off()  # Turn off the LED if command is recognized
                    print("Light turned OFF")
                else:
                    # Inform the user if the command is not recognized
                    print("Unknown command. Please say 'turn on the light' or 'turn off the light'.")

            # Exception handling for unrecognized speech
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Could you please repeat?")
            # Exception handling for connection issues with the speech recognition service
            except sr.RequestError as e:
                print(f"Error connecting to Google Speech Recognition service; {e}")

# Main function to initialize and start the program
def main():
    try:
        listen_and_control()  # Start listening for commands and controlling the LED
    except KeyboardInterrupt:
        # Cleanly exit the program when interrupted by the user
        print("Program stopped.")

# Ensure the program runs only if this file is executed directly
if __name__ == "__main__":
    main()
