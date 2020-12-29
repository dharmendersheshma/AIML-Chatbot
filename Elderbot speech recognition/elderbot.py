import aiml
import speech_recognition as sr
import time
import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()


# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

text = "dummy"
# Press CTRL-C to break this loop
while True:
    recognizer = sr.Recognizer()

    ''' recording the sound '''

    with sr.Microphone() as source:
        # print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Speak..")
        recorded_audio = recognizer.listen(source, timeout=None)
        # print("Done recording")

    ''' Recorgnizing the Audio '''
    try:
        # print("Recognizing the text")
        text = recognizer.recognize_google(
                recorded_audio,
                language="en-US"
            )
        print("You >> " + text)

    except Exception as ex:
        print(ex)

    # input_sentance = input("You >> ")
    output_sentence = kernel.respond(text)

    engine.say(output_sentence)
    print("Elderbot >> " + output_sentence)
    # play the speech
    engine.runAndWait()

    engine.stop()

    # time.sleep(2)
