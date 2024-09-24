import requests

def get_weather(city_name):
    api_key = "45db7d511f491ccaddc97edc24465de7"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Complete URL
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    # Sending GET request to the URL
    response = requests.get(complete_url)
    
    # Check if the response is valid
    if response.status_code == 200:
        data = response.json()
        
        # Extracting and printing the relevant data
        main = data['main']
        weather = data['weather'][0]
        
        print(f"City: {city_name}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found. Please enter a valid city name.")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)
