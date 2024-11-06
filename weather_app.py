import requests

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

city = input("Enter city name: ")
api_key = "f9de700b947c277c8dcefd57b35c1354"  # Replace this with your actual API key
print(get_weather(city, api_key))
