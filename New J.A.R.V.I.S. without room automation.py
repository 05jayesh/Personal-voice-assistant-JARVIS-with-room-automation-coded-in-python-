import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import re
import sys
import datetime
import math
voice = pyttsx3.init()
x=0
sn_command=('No data yet.')
sn2_command=('No data yet.')
answer=('No data yet')
saved_data=["" for x1 in range(150)]
saved_name=["" for x2 in range(150)]
i=0
j=0
shut_down=0
len_num=0

def assistant():
    global shut_down
    global calculate_command
    global len_num
    global answer
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Ready for command...')
        #r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('You said ' +command + '\n')

        if 'hello'in command or 'Hello' in command:
            talk('Hello sir!')
            return()
        elif 'who are you' in command:
            talk('I am Jarvis.')
            return()
        elif 'what is your name' in command:
            talk('My name is Jarvis.')
            return()
        elif 'you there' in command:
            talk('Yes Mr. Jayesh. I am right here.')
            return()
        elif 'how are you' in command:
            talk('I am good. Thankyou for asking.')
            return()
        elif 'you are not listening' in command:
            talk('Sorry sir. I am trying')
            return()
        elif 'listen' in command:
            talk('Yes sir! I am listening.')
            return()
        elif 'Google' in command or 'google' in command:
            google()
            return()
        elif 'YouTube' in command or 'youtube' in command or 'youTube' in command:
            youtube()
            return()
        elif 'thank' in command or 'Thank' in command:
            talk('Welcome')
            return()
        elif 'who made you' in command or 'who built you' in command:
            talk('Mr. Jayesh Prakash')
            return()
        elif 'time' in command or 'Time' in command:
            time()
            return()
        elif 'date' in command or 'Date' in command:
            date()
            return()
        elif 'day' in command or 'Day' in command:
            day()
            return()
        elif 'website' in command or 'Website' in command:
            website()
            return()
        elif 'calculate' in command or 'calculator' in command or 'Calculator' in command or 'Calculate' in command or 'calculation' in command or 'Calculation' in command or 'math' in command or 'Math' in command:
            talk('What do you want to calculate.')
            return()
        elif 'save' in command or 'shave' in command or 'Save' in command or 'record' in command or 'remember' in command or 'note' in command or 'Note' in command:
            save_number()
            return()
        elif 'recall' in command or 'notepad' in command or 'notebook' in command or 'remind' in command:
            recall()
            return()
        elif 'shut down' in command or 'shutdown' in command or 'Shutdown' in command or 'Shut down' in command:
            talk('Shutting down. Goodbye.')
            shut_down=1
            return()
        elif 'Jarvis' in command or 'jarvis' in command:
            talk('Yes Mr. Jayesh!')
            return()
        elif '!' in command or 'factorial' in command or 'Factorial' in command or '%' in command or 'percent' in command or 'Percent' in command or 'c' in command or 'C' in command or 'see' in command or 'See' in command or 'n' in command or 'N' in command or 'an' in command or 'An' in command or 'sin' in command or 'Sin' in command or 'Sigh' in command or 'sigh' in command or 'repeat' in command or 'Repeat' in command or 'cos' in command or 'Cos' in command or 'tan' in command or 'Tan' in command or '+' in command or 'add' in command or 'Add' in command or 'plus' in command or 'Plus' in command or '-' in command or 'minus' in command or 'Minus' in command or 'subtract' in command or 'Subtract' in command or 'multiply' in command or 'Multiply' in command or 'times' in command or 'into' in command or '*' in command or 'x' in command or 'X' in command or 'product' in command or 'Product' in command or '/' in command or 'divide' in command or 'Divide' in command or 'by' in command or 'By' in command or 'cube' in command or 'Cube' in command or 'log' in command or 'Log' in command or 'Logue' in command or 'logue' in command or 'root' in command or 'Root' in command or 'Route' in command or 'route' in command or 'Square' in command or 'square' in command or 'Power' in command or 'power' in command:
            calculate_command=command
            calculator()
            return()
        else:
            talk('Sorry I didn\'t recognised.')
            return()       
    except sr.UnknownValueError:
        return()        

def google():
    global x
    talk('Opening google')
    UC_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    url = 'https://www.google.com/'
    webbrowser.register('uc', None,webbrowser.BackgroundBrowser(UC_path))
    webbrowser.get('uc').open(url)
    talk('What do you want to search')
    g = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        g_audio = g.listen(source)
    try:
        google_command = g.recognize_google(g_audio)
        print('You said: ' + google_command + '\n')
        google_url = ('https://www.google.com/search?source=hp&ei=JRu3XO_QJsXZvgTwp6XQBQ&q=' + google_command )
        webbrowser.get('uc').open(google_url)
        talk('Done.  The results are on your screen.')
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        if x==1:
            x=0
            talk('Sorry! Can\'t hear you ')
            assistant()
        if x<1:
            x=x+1
            google()

def youtube():
    global x
    talk('Opening Youtube')
    UC_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    url = 'https://www.youtube.com/'
    webbrowser.register('uc', None,webbrowser.BackgroundBrowser(UC_path))
    webbrowser.get('uc').open(url)
    talk('Done. What videos do you want to search.')
    y = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        y_audio = y.listen(source)
    try:
        youtube_command = y.recognize_google(y_audio)
        print('You said: ' + youtube_command + '\n')
        google_url = ('https://www.youtube.com/results?search_query=' + youtube_command )
        webbrowser.get('uc').open(google_url)
        talk('Done.  The results are on your screen.')
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        if x==1:
            x=0
            talk('Sorry! Can\'t hear you ')
            assistant()
        if x<1:
            x=x+1
            google()
            
def website():
    global x
    talk('What website do you want me to open?')
    UC_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('uc', None,webbrowser.BackgroundBrowser(UC_path))
    w = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        w_audio = w.listen(source)
    try:
        website_command = w.recognize_google(w_audio)
        print('You said: ' + website_command + '\n')
        google_url = ('https://www.' + website_command )
        webbrowser.get('uc').open(google_url)
        talk('Done.  Opened ' + website_command)
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        if x==1:
            x=0
            talk('Sorry! Can\'t hear you ')
            assistant()
        if x<1:
            x=x+1
            website()

def save_number():
    global x
    global sn_command
    global saved_data
    global saved_name
    global i
    global j
    talk('Speak whatever you want to save or record.')
    sn = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        sn_audio = sn.listen(source)
    try:
        sn_command = sn.recognize_google(sn_audio)
        print('You said: ' + sn_command + '\n')
        talk('Done recording.')
        saved_data[i]=sn_command
        save_name()
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        if x==1:
            x=0
            talk('Sorry! Can\'t hear you ')
            assistant()
        if x<1:
            x=x+1
            save_number()
def save_name():
    global x
    global sn2_command
    global saved_data
    global saved_name
    global i
    global j
    talk('What do you want to save this as?')
    sn2 = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        sn2_audio = sn2.listen(source)
    try:
        sn2_command = sn2.recognize_google(sn2_audio)
        print('You said: ' + sn2_command + '\n')
        saved_name[i]=sn2_command
        i=i+1
        talk('Saved as' + sn2_command)
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        if x==1:
            x=0
            talk('Sorry! Can\'t hear you ')
            assistant()
        if x<1:
            x=x+1
            save_name()

def recall():
    global x
    global sn2_command
    global saved_data
    global saved_name
    global i
    global j
    talk('Which data do you want to recall?')
    rc = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        rc_audio = rc.listen(source)
    try:
        rc_command = rc.recognize_google(rc_audio)
        print('You said: ' + rc_command + '\n')
        j=0
        while j<100:
            if saved_name[j] in rc_command:
                print('The data saved as ', rc_command , ' is: ' , saved_data[j])
                talk('The data saved as ' + rc_command )
                talk(' is: ' + saved_data[j])
                j=0
                break
            else:
                j=j+1
        if j==100:
            talk('Sorry can\'t recognise.')
            j=0
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        if x==1:
            x=0
            talk('Sorry! Can\'t hear you ')
            assistant()
        if x<1:
            x=x+1
            recall()
            
def date():
    current_date=datetime.datetime.now()
    date_now = (current_date.strftime("%d, %B, %Y"))
    talk('The date is ' + date_now)
    
def day():
    current_day=datetime.datetime.now()
    day_now = (current_day.strftime("%A"))
    talk('The day is ' + day_now)
    
def time():
    current_time=datetime.datetime.now()
    time_now = (current_time.strftime("%I:%M, %p"))
    talk('The time is ' + time_now)
    
def calculator():
    global calculate_command
    global len_num
    global answer
    strl=calculate_command
    len_num=0
    number=(re.findall(r"[-+]?\d*\.\d+|\d+",strl))
    print('length of x = ',len(number))
    len_num=len(number)
    if 'sin' in calculate_command or 'Sin' in calculate_command or 'Sign' in calculate_command or 'sign' in calculate_command:
        if len_num<1:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            if 'inverse' in calculate_command:
                if '-' in calculate_command or 'minus' in calculate_command:
                    n1=-n1
                    if n1<-1:
                        print('Sorry! Can\'t calculate.')
                        talk('Sorry! Can\'t calculate')
                else:
                    n1=n1
                    if n1>1:
                        print('Sorry! Can\'t calculate.')
                        talk('Sorry! Can\'t calculate')
                ans=math.asin(n1)
                ans=((ans/(22/7))*180)
            else:
                if '-' in calculate_command or 'minus' in calculate_command:
                     n1=-n1
                else:
                    n1=n1
                ans=math.sin(n1)
                n1=(n1*((22/7)/180))
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(calculate_command, ' equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(calculate_command, 'equals to minus' , ans)
                talk(calculate_command + answer)
        return()
    elif 'cos' in calculate_command or 'Cos' in calculate_command:
        if len_num<1:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            if 'inverse' in calculate_command:
                if '-' in calculate_command or 'minus' in calculate_command:
                    n1=-n1
                    if n1<-1:
                        print('Sorry! Can\'t calculate.')
                        talk('Sorry! Can\'t calculate')
                else:
                    n1=n1
                    if n1>1:
                        print('Sorry! Can\'t calculate.')
                        talk('Sorry! Can\'t calculate')
                ans=math.acos(n1)
                ans=((ans/(22/7))*180)
            else:
                if '-' in calculate_command or 'minus' in calculate_command:
                    n1=-n1
                else:
                    n1=n1
                ans=math.cos(n1)
                n1=(n1*((22/7)/180))
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(calculate_command , ' equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(calculate_command , 'equals to minus' , ans)
                talk(calculate_command + answer)
        return()
    elif 'tan' in calculate_command or 'Tan' in calculate_command:
        if len_num<1:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            if 'inverse' in calculate_command:
                if '-' in calculate_command or 'minus' in calculate_command:
                    n1=-n1
                else:
                    n1=n1
                ans=math.atan(n1)
                ans=((ans/(22/7))*180)
            else:
                if '-' in calculate_command or 'minus' in calculate_command:
                    n1=-n1
                else:
                    n1=n1
                ans=math.tan(n1)
                n1=(n1*((22/7)/180))
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(calculate_command, ' equals to ' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(calculate_command , 'equals to minus' , ans)
                talk(calculate_command + answer)
        return()
    elif '*' in calculate_command or 'into' in calculate_command or 'x' in calculate_command or 'X' in calculate_command or 'times' in calculate_command or 'multiply' in calculate_command or 'product' in calculate_command or 'time' in calculate_command:
        if len_num<2:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            n2=float(number[1])
            ans=float(n1*n2)
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(n1 , 'multiplied by ' , n2 , 'equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(n1 , 'multiplied by ' , n2 , 'equals to minus ' , ans)
                talk(calculate_command + answer)
        return()
    elif '/' in calculate_command or 'by' in calculate_command or 'divide' in calculate_command:
        if len_num<2:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            n2=float(number[1])
            ans=float(n1/n2)
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(n1 , 'divided by ' , n2 , 'equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(n1 , 'divided by ' , n2 , 'equals to minus ' , ans)
                talk(calculate_command + answer)
        return()
    elif '+' in calculate_command or 'add' in calculate_command or 'plus' in calculate_command:
        if len_num<2:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            n2=float(number[1])
            ans=float(n1+n2)
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(n1 ,'plus ', n2 ,'equals to', ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(n1 ,'plus ', n2 ,'equals to minus ', ans)
                talk(calculate_command + answer)
        return()
    if '-' in calculate_command or 'minus' in calculate_command or 'subtract' in calculate_command:
        if len_num<2:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            n2=float(number[1])
            if 'from' in calculate_command:
                num1=str(n2)
                num2=str(n1)
            else:
                num1=str(n1)
                num2=str(n2)
            ans=float(n1-n2)
            answer=str(ans)
            minus_command=(num1 + ' minus ' + num2)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(n1 , 'minus ' , n2 , 'equals to' , ans)
                talk(minus_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(n1 , 'minus ' , n2 , 'equals to minus  ' , ans)
                talk(minus_command + answer)
        return()
    elif 'cube root' in calculate_command or 'cube Root' in calculate_command or 'cube Route' in calculate_command or 'cube route' in calculate_command:
        if len_num<1:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            ans=n1**(1/3)
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print('Cube root of ' , n1 , 'equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equal to minus' + answer)
                print('Cube root of '  ,n1 , 'equals to minus ' , ans)
                talk(calculate_command + answer)
        return()
    elif 'power' in calculate_command or 'Power' in calculate_command:
        if len_num<2:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            n2=float(number[1])
            ans=n1**n2
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(n1 , 'power ' , n2 , 'equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(n1 , 'power ' , n2 , 'equals to minus' , ans)
                talk(calculate_command + answer)
        return()
    elif '%' in calculate_command or 'percent' in calculate_command or 'Percent' in calculate_command:
        if len_num<2:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            n2=float(number[1])
            ans=((n1*n2)/100)
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(n1 , ' percent of ' , n2 , 'equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(n1 , ' percent of ' , n2 , 'equals to minus' , ans)
                talk(calculate_command + answer)
        return()
    elif 'Square' in calculate_command or 'square' in calculate_command:
        if len_num<1:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            ans=n1*n1
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print(n1 , 'square equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print(n1 , 'square equals to minus' , ans)
                talk(calculate_command + answer)
        return()
    elif 'root' in calculate_command or 'route' in calculate_command or 'Root' in calculate_command or 'Route' in calculate_command:
        if len_num<1:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            ans=math.sqrt(n1)
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print('root of ' , n1 , 'equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print('root of ' , n1 , 'equals to minus' , ans)
                talk(calculate_command + answer)
        return()
    elif '!' in calculate_command or 'Factorial' in calculate_command or 'factorial' in calculate_command:
        if len_num<1:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            if n1<0:
                print('Sorry! Can\'t calculate.')
                talk('Sorry! Can\'t calculate')
            else:
                ans=math.factorial(n1)
                answer=str(ans)
                if ans>=0:
                    answer=(' equals to ' + answer)
                    print('Factorial of ' , n1 , 'equals to' , ans)
                    talk(calculate_command + answer)
                else:
                    ans=0-ans
                    answer=('equals to minus' + answer)
                    print('Factorial of ' , n1 , 'equals to minus' , ans)
                    talk(calculate_command + answer)
        return()
    elif 'log' in calculate_command: 
        if len_num<1:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            if 'natural' in calculate_command:
                ans=math.log(n1)
                answer=str(ans)
            else:
                ans=math.log10(n1)
                answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print('log of ' , n1 , 'equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print('log of ' , n1 , 'equals to minus' , ans)
                talk(calculate_command + answer)
        return()
    elif 'cube' in calculate_command or 'Cube' in calculate_command:
        if len_num<1:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            ans=n1*n1*n1
            answer=str(ans)
            if ans>=0:
                answer=(' equals to ' + answer)
                print('cube of ' , n1 , 'equals to' , ans)
                talk(calculate_command + answer)
            else:
                ans=0-ans
                answer=('equals to minus' + answer)
                print('cube of ' , n1 , 'equals to minus' , ans)
                talk(calculate_command + answer)
        return()
    elif 'Repeat' in calculate_command or 'repeat' in calculate_command:
        talk(answer)
        return()
    elif 'c' in calculate_command or 'C' in calculate_command or 'See' in calculate_command or 'see' in calculate_command:
        if len_num<2:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            n2=float(number[1])
            if (n1-n2)<0:
                print('Sorry! Can\'t calculate.')
                talk('Sorry! Can\'t calculate.')
            else:
                ans=((math.factorial(n1))/((math.factorial(n1-n2))*(math.factorial(n2))))
                answer=str(ans)
                if ans>=0:
                    answer=(' equals to ' + answer)
                    print(n1 , ' C ' , n2 , 'equals to' , ans)
                    talk(calculate_command + answer)
                else:
                    ans=0-ans
                    answer=('equals to minus' + answer)
                    print(n1 , ' C ' , n2 , 'equals to minus' , ans)
                    talk(calculate_command + answer)
        return()
    elif 'n' in calculate_command or 'N' in calculate_command or 'an' in calculate_command or 'An' in calculate_command:
        if len_num<2:
            print('Sorry! Can\'t recognise.')
            talk('Sorry! Can\'t recognise.')
        else:
            n1=float(number[0])
            n2=float(number[1])
            if (n1-n2)<0:
                print('Sorry! Can\'t calculate.')
                talk('Sorry! Can\'t calculate.')
            else:
                ans=((math.factorial(n1))/(math.factorial(n1-n2)))
                answer=str(ans)
                if ans>=0:
                    answer=(' equals to ' + answer)
                    print(n1 , 'N ' , n2 , 'equals to' , ans)
                    talk(calculate_command + answer)
                else:
                    ans=0-ans
                    answer=('equals to minus' + answer)
                    print(n1 , ' N ' , n2 , 'equals to minus' , ans)
                    talk(calculate_command + answer)
        return()
    else:
        talk('Sorry I didn\'t recognized. Try again.')
        return()
    return()

def talk(audio):
    print(audio)
    voice.say(audio)
    voice.runAndWait()
    
talk('Jarvis here!')
while True:
    if shut_down==1:
        break
    else:
        assistant()
