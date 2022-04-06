tod_dict = {'00': 'night', '01': 'Ahri_Popstar_30599', '02': 'ночь',
            '03': 'раннее утро', '04': 'раннее утро', '05': 'раннее утро',
            '06': 'утро', '07': 'утро', '08': 'утро',
            '09': 'первая половина дня', '10': 'первая половина дня', '11': 'первая половина дня',
            '12': 'обед', '13': 'обед', '14': 'обед',
            '15': 'после обеда', '16': 'после обеда', '17': 'после обеда',
            '18': 'Ahri_Popstar_30599', '19': 'Ahri_Popstar_30599', '20': 'Ahri_Popstar_30599',
            '21': 'Ahri_Popstar_30599', '22': 'поздний вечер', '23': 'поздний вечер'}




def tick():
    watch.after(200, tick)
    watch['text'] = time.strftime("%H:%M:%S")
    watch_hours = time.strftime("%H")
    for val, key in tod_dict.items():
        if int(watch_hours) == int(val):
            print(val, key)
            photo = Image.open(f"{Path.cwd()}/" + tod_dict[val] + ".png")
            img = photo.resize((width, height))
            image = ImageTk.PhotoImage(img)
            l_image = ttk.Label(top_frame, image=image)
            l_image.place(relwidth=0.3, relheight=0.2)

            # img = Image.open(f"{Path.cwd()}/{tod_dict[val]}.png")
            # print(f"{Path.cwd()}/{tod_dict[val]}.png")

watch = Label(top_frame, font="Arial 25")
watch.pack(expand=1)
watch.after_idle(tick)


{'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'облачно с прояснениями', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': -1.71, 'feels_like': -4.41, 'temp_min': -1.97, 'temp_max': -0.9, 'pressure': 1004, 'humidity': 88, 'sea_level': 1004, 'grnd_level': 986}, 'visibility': 10000, 'wind': {'speed': 1.97, 'deg': 226, 'gust': 4.44}, 'clouds': {'all': 80}, 'dt': 1649269538, 'sys': {'type': 2, 'id': 47754, 'country': 'RU', 'sunrise': 1649213274, 'sunset': 1649261745}, 'timezone': 10800, 'id': 524901, 'name': 'Москва', 'cod': 200}
