# pip install ttkthemes
# pip install requests
# pip install translate
import time
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
from tkinter import messagebox
from translate import Translator
import requests
from pathlib import Path

API_KEY = '7a8289c6fe2c48775c4d2464078220be'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

width = 80
height = 80

translator = Translator(from_lang='Russian', to_lang='English')  # язык для перевода  на английский


def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        press = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']
        sunrise = time.strftime("%H:%M:%S", time.localtime(weather['sys']['sunrise']))
        sunset = time.strftime("%H:%M:%S", time.localtime(weather['sys']['sunset']))
        return f"Местоположение: {city}, {country} \nТемпература: {temp} °С \nАтм. давление: {press} гПа \nВлажность: {humidity}% \nСкорость ветра: {wind} м/с \nПогодные условия {desc} \nВосход: {sunrise} \nЗакат {sunset}"
    except:
        return "Ошибка получения данных..."


def get_weather(event=''):
    if not entry.get():
        messagebox.showwarning("Warning", 'Введите запрос в формате город, код города')
    else:
        params = {
            "appid": API_KEY,
            "q": translator.translate(entry.get()),
            "units": "metric",
            "lang": "ru"
        }
        r = requests.get(API_URL, params=params)
        weather = r.json()
        label['text'] = print_weather(weather)


root = ThemedTk(theme="arc")
root.geometry("400x500")
root.title("Погода")
root.resizable(False, False)
root.iconbitmap(f'{Path.cwd()}/cloud.ico')

s = ttk.Style()
s.configure("TLabel", padding=5, font="Arial 11")
top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.7, relheight=1)

button = ttk.Button(top_frame, text="Запрос погоды", command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

# translation = translator.translate("Москва")

lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(lower_frame, anchor="nw")
label.place(relheight=1, relwidth=1)

entry.bind("<Return>", get_weather)

root.mainloop()
