import speech_recognition as sr 
import time
import webbrowser
import os
import datetime
from openai import OpenAI
from keys import apikey
from newsapi import NewsApiClient
import requests

client = OpenAI(api_key=apikey)
finalChat = ""
j = 1                       # This is just for the news Headline Counter 

def say(text):
    os.system(f'say "{text}"')

# Completing tasks using Open Ai's api key (Eg: Writing an email to a teacher for assignment extension)
def usingAIForPrompt(order):
    response = client.chat.completions.create(
    model="gpt-4o-mini",  
    messages=[
            {"role": "user", "content": order}
        ]
    )
    forFile = f"OpenAI response for the prompt: {order}\n**************************\n"
    forFile += response.choices[0].message.content
    with open (f"OpenAI/{order.split("intelligence")[1].strip()}.txt", "w") as file: # Storing as per prompt in a file
        file.write(forFile) 
    return (response.choices[0].message.content)

# ChatBot functionalities
def chatBot(chatMsg): 
    global finalChat
    finalChat = f"Saksham: {chatMsg}\nAssistant: "
    response = client.chat.completions.create(
    model="gpt-4o-mini",  
    messages=[
            {"role": "user", "content": finalChat}
        ]
    )
    requiredResponse = response.choices[0].message.content
    say(requiredResponse)
    print(finalChat+requiredResponse)
    return requiredResponse

# Getting the coordinates of the city said, knowing the weather, and reporting the weather at that city

def getCoordinates(prompt):
    global lat, lon, city
    city = prompt.split(" ")[2]
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params= {
        "name": city, "count": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    lat = data['results'][0]['latitude']
    lon = data['results'][0]['longitude']
    getWeather()
    return lat, lon

def getWeather(): 
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat, 
        "longitude": lon, 
        "hourly": "temperature_2m",
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    weatherData = response.json()
    report = f"{(weatherData["hourly"]["time"][3:4])}: {weatherData["hourly"]["temperature_2m"][3:4]}"
    reportWeather(report)
    return   

def reportWeather(report): 
    reportPrompt = f"Report this weather data at {city} nicely: {report}" # Reporting the weather using GPT 4 
    response = client.chat.completions.create(
    model="gpt-4o-mini",  
    messages=[
            {"role": "user", "content": reportPrompt}
        ]
    )
    reqReport = response.choices[0].message.content
    say(reqReport)
    return reqReport

# Integrating the news API into our desktop assistant 
def getNews(): 
    global j                                        # Just for the news headline counter, optional
    newsapi = NewsApiClient(api_key='Insert your api key here')
    all_articles = newsapi.get_everything(
    q='bitcoin',
    language='en',
    sort_by='relevancy',
    page_size=10
    )
    print("\t\t\t---------- ****** Here are some headlines with their respective urls ***** ----------\n\n")
    for i in all_articles['articles']: 
        print(f"{j}. {i['title']}\n----->For more information go to: {i['url']}\n")
        j+=1
    return      
       

# This is the main section that takes in the command and passes it to the recurring while loop in the end
def command(): 
    recog = sr.Recognizer()
    with sr.Microphone() as source: 
        try: 
            time.sleep(1)
            print("Recognizing...")
            inPut = recog.listen(source)
            text = recog.recognize_google(inPut, language="en-in")
            print(f"The user said: {text}")
            return text 
        except Exception as e: 
            return "Some error occured. Please try again!"

say ("Assistant here")

while True: 
    print("Listening...")
    prompt = command().lower()
    sites = [["youtube", "https://youtube.com"], ["google", "https://google.com"], "wikipedia", "https://wikipedia.com"]
    for site in sites: 
        if f"Open {site[0]}".lower() in prompt: 
            say(f"Opening {site[0]} sir")
            webbrowser.open(site[1])
    if "Open music".lower() in prompt: 
            say("Opening music sir")
            os.system("open '/Users/sakshamdhakal/Desktop/Web Projects/Spotify Clone/songs/FirstSet/Comethru-Jeremy Zucker.mp3'")
    elif "time".lower() in prompt:
            say("Displaying the time")
            timeIs = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {timeIs}")
        # Integrating OpenAI into our prompt
    elif "Artificial intelligence".lower() in prompt: 
            usingAIForPrompt(prompt)
    elif "exit".lower() in prompt: 
            exit()
    elif ("weather in".lower() or "weather of". lower()) in prompt: 
            getCoordinates(prompt)
    elif ("news today".lower()) in prompt: 
         getNews()
    else: 
        chatBot(prompt)

          



