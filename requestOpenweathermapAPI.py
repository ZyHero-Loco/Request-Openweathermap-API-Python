import json, requests #python -m pip install requests

API_KEY = input("Openweathermap.org api key: ").strip()

cities = ["London,uk" , "Palatine,us", "Chicago"]

CITY_NAME = input("City: ") #cities[2] 

def printWeatherData(data):
    #print(data['weather'][0]['main'])
    print("Current weather in " + CITY_NAME + " is " + data['weather'][0]['main'] + " specifically " + data['weather'][0]['description'])
    return 0

if API_KEY.lower() != "api key":
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&APPID={API_KEY}'
    del(API_KEY) #Do not remember api key
    
    response = requests.get(api_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        #print(data)
        printWeatherData(data)
    else: 
        print("Error: ", response.status_code)
    ##Extra for saving information to a file, then re-enter api key to load the information from the file
    #''' 
    #output = open("response.json", "w")
    #output.write(response.text) 
#else:
    ##if api key is api key then open previously saved data
    #response = open("response.json", "r")
    #print(response.readline())
    #data = json.load(response)
    ##print(data)
    #printWeatherData(data)
    ##subprocess.Popen([r"C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2307.27.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe",r"response.json"])
##'''
