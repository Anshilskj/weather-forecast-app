import tkinter as tk
import requests

# Function to get weather from the API
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        return f"Weather in {city}: {temperature}°C, {description.capitalize()}"
    else:
        return "City not found."

# Function to display the weather in the label
def show_weather():
    city = city_entry.get()  # Get city name from the input field
    api_key = "f9de700b947c277c8dcefd57b35c1354"  # Replace this with your actual API key
    result = get_weather(city, api_key)
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x300")  # You can adjust the size based on your preferences

# Create a label for the title
title_label = tk.Label(root, text="Weather Forecast", font=("Arial", 18))
title_label.pack(pady=10)

# Create an entry widget to enter the city name
city_label = tk.Label(root, text="Enter city name:")
city_label.pack()
city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=5)

# Create a button to fetch weather data
fetch_button = tk.Button(root, text="Get Weather", command=show_weather)
fetch_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()