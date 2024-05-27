#this program is written by muhammad yousaf Email:yousafsahiwal3@gmail.com
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap 

screen = ttkbootstrap .Window(themename="morph")
screen.title("BreezyBytes by Muhammad Yousaf")
screen.geometry("400x400")

def get_weather(city):
    api_key = "d118360a25ccf15c1c39b8621d4bd175"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    res = requests.get(url)
    if res.status_code == 404:
        messagebox.showerror("ERROR", "City not found")
        return None
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

def search():
    city = cn.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url, temperature, description, city, country = result
    ll.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    il.configure(image=icon)
    il.image = icon

    temp_l.configure(text=f"Temperature: {temperature:.2f}°C")
    descp_l.configure(text=f"Description: {description}")

cn = ttkbootstrap .Entry(screen, font=("Helvetica", 18))
cn.pack(pady=10)

sb = ttkbootstrap .Button(screen, text="Search", command=search, bootstyle="warning")
sb.pack(pady=10)

ll = tk.Label(screen, font=("Helvetica", 25))
ll.pack(pady=20)

il = tk.Label(screen)
il.pack()

temp_l = tk.Label(screen, font=("Helvetica", 20))
temp_l.pack()

descp_l = tk.Label(screen, font=("Helvetica", 20))
descp_l.pack()

screen.mainloop()

