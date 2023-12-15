import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import pywhatkit
import webbrowser
import os
import smtplib
from datetime import date
from PIL import Image
import random
from PIL import ImageGrab
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

is_muted = False


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 
        
    speak(" matrix at you service sir, how may i help you ")       
   
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if is_muted:
            print("Muted. Say 'wakeup' to resume listening.")
            audio = r.listen(source, timeout=None)
        else:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in''hi')
        print(f"You : {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"

def mute():
    global is_muted
    is_muted = True
    speak("Muted")

def unmute():
    global is_muted
    is_muted = False
    speak("Resuming listening")

def greeting():
    reply_greetings = ["Hello","Hi","Hola","hey","hey there","yes sir","at your service"]
    reply = random.choice(reply_greetings)
    speak(reply)

def ask_health():
    reply_health = ["I am fine","Doing well", "Feeling good today","As good as new","Awesome","fantastic","Outstanding","Astounding","Great","energetic"]
    health = random.choice(reply_health)
    speak(health)
    
def tellJoke():
    jokes = [
        "Why did the computer catch a cold? Because it had too many windows open!",
        "Why don't programmers like nature? It has too many bugs.",
        "I'm not a programmer; I'm a chameleon. I can blend in with any environment.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "I'm not lazy; I'm just on my energy-saving mode.",
        "Dear math , grow up and solve your own problems"
    ]
    
    joke = random.choice(jokes)
    speak(joke)

def YoutubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(result)
    speak("this is what i found from your search")
 
def compliments():
    compliment_reply = ["always ready for you sir","welcome sir","anything","anytime","worth the help sir"]      
    compliment = random.choice(compliment_reply)
    speak(compliment)
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube now')
            
        elif "hello" in query or "hi" in query or "hey" in query or "matrix" in query or "hola" in query or "wakeup" in query or "mat" in query or "machine" in query or "hey there" in query:
           greeting()
        
        elif "how are you" in query or "how do you do" in query or "health" in query or "hope you fine" in query or 'stats' in query:
            ask_health()
            
        elif 'are you there' in query:
            speak('yes sir . always ready')  
        
        elif 'tell me a joke' in query:
            tellJoke()              
 
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google now')

        elif 'what is your name' in query:
            speak('my name is matrix . iam a virtual machine designed to take over orders by user . i was created by saamphath kumaar .')    
        
        elif 'who is your creator' in query:
            speak(' i was created by saamphath kumar')
        
        elif 'search the item said ' in query:
            speak('im ready to search whatever you say sir')    
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak('opening stack overflow website now') 
        
        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'give me data' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())
            
        elif 'open maps' in query:
            webbrowser.open("maps.google.com")
            speak('opening maps now')      
        
        elif 'mute' in query:
            mute()
            
        elif 'wake up' in query:
            unmute()        
               
        elif 'open chrome' in query:
            webbrowser.open("chrome.com")  
            speak('opening chrome now')  
        
        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'what is the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open my study folder' in query:
            os.startfile('C:\\Users\\sampathkumar\\OneDrive\\Desktop\\LIBRARY')   
            
        elif 'what day is today' in query:
            day = datetime.datetime.today().weekday() +1
            Day_dict = {1: 'monday', 2: 'tuesday' , 3: 'wednesday' , 4: 'thursday' , 5: 'friday' , 6: 'saturday' , 7: 'sunday'}
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak('sir , the day is ' + day_of_the_week)
                 
        elif 'what is the date' in query:
            today_date = date.today()
            speak('sir today date is')
            print(today_date)
            speak(today_date) 
        
        elif 'open visual studio' in query or 'open coding platform' in query:
            codePath = "C:\\Users\\sampathkumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to somebody' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sampathhungund@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
        
        elif 'thank you'in query or 'good job' in query or 'well done' in query or 'good' in query:
                compliments()                 
        
        elif 'open editor' in query:
            os.startfile("D:\\adobe\\Adobe\\Adobe After Effects 2020\\Support Files\\AfterFX.exe")
        
        elif 'open blender' in query:
            os.startfile("D:\\BLENDER\\blender.exe")     
        
        elif'show my exam schedule' in query:
            speak('The exam will be scheduled soon based on the college information')    
        
        elif 'play my track' in query or 'play music' in query:
            os.startfile("D:\\music\\Die For You.mp3")  
            speak('playing the music , Die for you')
        
        elif 'open screen recorder' in query:
            os.startfile("D:\\SETUPS\\obs\\obs-studio\\bin\\64bit\\obs64.exe")        
        
        elif 'open snipping tool' in query:
            os.system("start snippingtool")
        
        elif 'take a screenshot' in query:
            screenshot = ImageGrab.grab()
            screenshot.save("screenshot.png")
            screenshot.show()
            
            image_path = 'path/to/your/image.jpg'
            img = Image.open(image_path)
            img.show()
            closing_time = 5
            time.sleep(closing_time)
            img.close()
        
        elif 'search google' in query:
            import wikipedia as googleScrap
            query = query.replace("matrix","")
            query = query.replace("google search","")
            query = query.replace("google","")
            pywhatkit.search(query)
            speak("this is what i found , sir")
            
            try:
                result= googleScrap.summary(query,3)
                speak(result)
                
            except:
                speak("the call was not successfull , sir") 
            



                            
                        