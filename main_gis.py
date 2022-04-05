# pip install ttkthemes
# pip install requests
# pip install translate
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
from tkinter import messagebox
from translate import Translator
from pathlib import Path
import time
from PIL import Image, ImageTk

tod_dict = {'00': 'night', '01': 'Ahri_Popstar_30599', '02': 'ночь',
            '03': 'раннее утро', '04': 'раннее утро', '05': 'раннее утро',
            '06': 'утро', '07': 'утро', '08': 'утро',
            '09': 'первая половина дня', '10': 'первая половина дня', '11': 'первая половина дня',
            '12': 'обед', '13': 'обед', '14': 'обед',
            '15': 'после обеда', '16': 'после обеда', '17': 'после обеда',
            '18': 'вечер', '19': 'вечер', '20': 'вечер',
            '21': 'поздний вечер', '22': 'поздний вечер', '23': 'поздний вечер'}

API_KEY = '7a8289c6fe2c48775c4d2464078220be'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

width = 80
height = 80

def get_weather():
    pass


def tick():
    watch.after(200, tick)
    watch['text'] = time.strftime("%H:%M:%S")
    watch_hours = time.strftime("%H")
    for val, key in tod_dict.items():
        if int(watch_hours) == int(val):
            print(val, key)
            photo = Image.open(f"{Path.cwd()}/{tod_dict[val]}.png")
            img = photo.resize((width, height))
            image = ImageTk.PhotoImage(img)
            l_image = ttk.Label(top_frame, image=f'{image}')
            l_image.place(relwidth=0.3, relheight=1)
            # img = Image.open(f"{Path.cwd()}/{tod_dict[val]}.png")
            # print(f"{Path.cwd()}/{tod_dict[val]}.png")


root = ThemedTk(theme="ark")
root.geometry("500x500")
root.title("Погода")
root.resizable(False, False)
root.iconbitmap(f'{Path.cwd()}/cloud.ico')
top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.2, anchor='n')
watch = ttk.Label(top_frame, font="Arial 25")
watch.pack(expand=1)
watch.after_idle(tick)


bottom_frame = ttk.Frame(root)
bottom_frame.place(relx=0.5, rely=0.3, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(bottom_frame)
entry.place(relwidth=0.7, relheight=1)

button = ttk.Button(bottom_frame, text="Запрос погоды", command=get_weather)
button.place(relwidth=0.3, relheight=1)

translator = Translator(from_lang='Russian', to_lang='English')  # язык для перевода  на английский
# translation = translator.translate("Москва")


root.mainloop()
