
import requests
import pyttsx3


def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        city = data.get("city")
        country = data.get("country")
        return city, country
    except:
        return None, None

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != 200:
        return None
    return data

def islamic_advice(weather):
    desc = weather["weather"][0]["main"].lower()
    if "rain" in desc:
        return "It will rain today — remember to make dua for Rahmah (mercy)."
    elif "clear" in desc:
        return "It's a clear sunny day — say Alhamdulillah for the blessing of light."
    elif "cloud" in desc:
        return "Cloudy skies today — Allah shades His servants with mercy."
    elif "wind" in desc:
        return "Windy weather — the Prophet ﷺ said: do not curse the wind, for it is from Allah."
    elif "storm" in desc:
        return "Stormy weather — seek protection by saying: Allahumma inni a'udhu bika min sharri hadha ar-reeh."
    else:
        return "Alhamdulillah for today's weather — every condition is by Allah's wisdom."

city, country = get_location()

if city:
    weather = get_weather(city)
    if weather:
        temp = weather["main"]["temp"]
        desc = weather["weather"][0]["description"]
        message = islamic_advice(weather)
        full_msg = f"In {city}, {country}: temperature is {temp}°C with {desc}. {message}"
        print(full_msg)
    else:
        print("Unable to get weather details.")
else:
    print("Could not detect location. Please check your internet connection!.")
