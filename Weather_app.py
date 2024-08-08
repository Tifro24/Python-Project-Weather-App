weather_data = { "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, 
                "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"}, 
                "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, 
                "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, 
                "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} }


print('*'* 50)
print('           ','Welcome to the Weather App!')
print('*'* 50)
print('')



def get_data():
    city = input("Please enter your city of choice: ")


    if city.lower().title() in weather_data: # .lower().title() to account for case sensitivity - needs to match the format of our dictionary cities
        temperature = weather_data[city.lower().title()]['temperature']
        conditions = weather_data[city.lower().title()]['conditions']
        wind_speed = weather_data[city.lower().title()]['wind_speed']
        humidity = weather_data[city.lower().title()]['humidity']

        print("")
        print(city.lower().title())
        print('Temperature: ',temperature, '\nConditions: ',conditions, '\nWind Speed: ',wind_speed, '\nHumidity: ',humidity )
        print("\nThank you for using the program!\n")
        ans = input("Would like to enter anothery city? Please enter Yes or No: ")
        if ans.lower() == 'yes':
            print('')
            get_data()
        elif ans.lower() == 'no':
            print("Thanks again and have a great day!")
            exit()
        else:
            print("That wasn't either of the options, but I'll take it as a no, have a great day!")
    else:
        print("This country is unfortunately not in our database. Please select from the list below\n")
        for city in weather_data:
            print(city)
        print("")
        get_data()
        
        

get_data()
        





