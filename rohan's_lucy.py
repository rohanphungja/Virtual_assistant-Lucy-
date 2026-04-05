
import os
os.environ["PATH"] += ":/opt/homebrew/bin"
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from openai import OpenAI



def speak(text): 
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def openai(command):
    # use your own api key here
    client = OpenAI(api_key=" ")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "You are virtual assistant named lucy developed by Rohan. You reply like Alexa and google cloud"},
            {"role": "user", "content": command}
            ]
    )
    return response.choices[0].message.content

def process_command(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("opening google")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("opening youtube")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("opening facebook")
    
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        speak("opening instagram")
    
    elif "open watsapp" in command:
        webbrowser.open("https://watsapp.com")
        speak("opening watsapp")
    elif "play" in command:
        song = command.split(" ")[1]
        link = musiclibrary.RohanFavouriteMusic[song]
        webbrowser.open(link)
    
    else:
        output = openai(command)
        speak(output)

print("Welcome to Rohan's lucy!")

if __name__ == "__main__":
    speak("This is lucy 2 point o, devloped by Rohan. Please say activation code ")
    while True:
        r = sr.Recognizer()    
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source ,timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "lucy activate"):
                    speak("Lucy activated. How can I assist you?")
                    while True:
                        with sr.Microphone() as source:
                            print("Lucy active......")
                            audio = r.listen(source,timeout=5, phrase_time_limit=5)
                            command = r.recognize_google(audio)
                            print(command)
                            if command.lower() == "lucy deactivate":
                                speak("Lucy deactivated")
                                quit()
                            else:
                                process_command(command)
                            
            elif "deactivate" in word.lower():
                    speak("Lucy deactivated")
                    break
    
            else:
                speak("That is not a activation code.")
                
        except sr.UnknownValueError:
            print("lucy could not understand audio")
        except sr.RequestError as e:
            print("lucy error; {0}".format(e))
        
