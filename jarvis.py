
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import cv2
import pyautogui
import openai
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id) -- mishra 
# engine.setProperty('voices', voices[0].id) -- mishra 

print(voices[1].id)  # Print the ID of the second voice
engine.setProperty('voice', voices[0].id)  # Set the voice property to the first voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #  audio = r.listen(source, timeout=1, phrase_time_limit = 5) -- mishra
        audio = r.listen(source, timeout=10, phrase_time_limit=5)  # Increased timeout to 10 seconds to make the model listen

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    #  added some more exception to handle network error and unknown errors
    except sr.UnknownValueError:
        speak("I did not understand that. Could you please repeat?")
        return "none"
    except sr.RequestError:
        speak("Could not request results; check your network connection.")
        return "none"
    except Exception as e:
        speak("Say that again please...")
        return "none"

    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morinig sir")
    elif hour>12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening")
    speak("jarvis reporting, how may I help u")


# # Define a function to interact with the API
# openai.api_key = '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'
# def ask_openai(prompt):
#          response = openai.Completion.create(
#          engine="text-curie-001",
#          prompt=prompt,
#          max_tokens=150)
                        
#          return response.choices[0].text.strip()
    


if __name__ == "__main__":
    # speak("hello sir, jarvis reporting , How may I hepl u, did you stuck to a problem , do not wory I can solve it, if you order")
    # take_command()
    wish()
    while True:
        query = take_command().lower()

        
        if "open notepad" in query:
            path= "C:\\Windows\\notepad.exe"
            speak("opening notepad")
            os.startfile(path)

        elif "open command prompt" in query:
           speak("opening command prompt")
           os.system("start cmd")
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                
                k = cv2.waitKey(50)
                if k==27 :
                    break;
        # cap.release()
        # cv2.destroyAllWindows()

    
        elif "can u play " in query or "play a song" in query or "please play a song" in query or "play" in query:
        #  speak("what u would like to listen")
        #  song= take_command()
         speak("ok here is your song")
         webbrowser.open(f"https://open.spotify.com/search/{query}")
         
         
        elif  "chat gpt" in query:
        #  speak("what u would like to listen")
        #  song= take_command()
         speak("why do u want chatgpt if i am there for u, but still opening chat gpt")
         webbrowser.open(f"https://chatgpt.com")

        elif  "youtube" in query:
        #  speak("what u would like to listen")
        #  song= take_command()

         speak("what do u want me to search in youtube")
         search=take_command()
         speak("ok, searching your request in youtube")
         webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
        
        # else:
        #     user_input = query
        #     print(ask_openai(user_input))
    #   just added a comment

          
       
        break






# >>>>>>> fb7034228916090870c2b4a530592a79ebe25ae2
"""//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button"""