import speech_recognition as sr
import pyttsx3
import openAIsys as opAI
import datetime

microphone = sr.Recognizer()
WAKE = "hey jennifer"
def SpeakText(command):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    voice = engine.getProperty('voices') 
    engine.setProperty('voice', voice[1].id)
    engine.say(command)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        SpeakText("Good Morning Sir ")
  
    elif hour>= 12 and hour<18:
        SpeakText("Good Afternoon Sir ")  
  
    else:
        SpeakText("Good Evening Sir ") 
  
    assname =("Jennifer")
    SpeakText("I am your Assistant")
    SpeakText(assname)
    
def start():
    wishMe()   
    while(1):
        
        try:
            with sr.Microphone() as Source2:
                microphone.adjust_for_ambient_noise(Source2, duration = 0.3)
                audio2 = microphone.listen(Source2)
                MyText = microphone.recognize_google(audio2)
                MyText = MyText.lower()
                

                        
                print(MyText)
                response = opAI.response_Summary(MyText)
                
                SpeakText(response)
                
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")
            
            
if __name__ == "__main__":
    start()