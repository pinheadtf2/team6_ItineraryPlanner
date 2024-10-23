from os import getenv
from dotenv import load_dotenv

from weather import get_weather
from resturaunts import find_nearby_restaurants
from attractions import get_nearby_attractions

att1 = ('name', 'rating', 'addr')
att2 = ('name', 'rating', 'addr')
att3 = ('name', 'rating', 'addr')
tempAttrac = (att1, att2, att3)


def getWeather(loc):
    print('===========================================')
    print(f'Weather for {loc.location["name"]}, {loc.location["region"]}, {loc.location["country"]}:')
    print(f'Current Conditions: {loc.condition} @ {loc.current_temperature}°F with wind speed of {loc.wind_speed} mph')
    print(f'Max: {loc.max_temperature}°F | Min: {loc.min_temperature}°F')
    print(f'Chance of Precipitation ({loc.precipitation_type}): {loc.precipitation_chance}%')


def getAttractions(lat, long, loc):
    attractions = get_nearby_attractions(getenv("RESTAURANTS_KEY"), latitude, longitude)
    print('===========================================')
    print('Things to do around ' + loc + ':\n')
    count = 0
    for attraction in attractions:
        print('Name: ' + attraction['name'])
        print(f'Rating: {attraction['rating']}')
        print('Address: ' + attraction['address'] + '\n')
        count += 1
        if count % 3 == 0:
            userChoice = input('Show more? (Y|n)')
            if (userChoice == 'n'): break
            elif (userChoice != 'Y' or userChoice != 'y'): 
                print('-------------------------------------------')
            elif (userChoice != 'n' and userChoice != 'Y'):
                print('Invalid input, continuing by default')

def getFood(lat, long, loc):
    restaurants = find_nearby_restaurants(getenv("RESTAURANTS_KEY"), lat, long)
    print('===========================================')
    print('Places to eat ' + loc + ':\n')
    count = 0
    for restaurant in restaurants:
        print('Name: ' + restaurant['name'])
        print(f'Rating: {restaurant['rating']}')
        print('Address: ' + restaurant['address'] + '\n')
        count += 1
        if count % 3 == 0:
            userChoice = input('Show more? (Y|n)')
            if (userChoice == 'n'): break
            elif (userChoice != 'Y' or userChoice != 'y'): 
                print('-------------------------------------------')
            elif (userChoice != 'n' and userChoice != 'Y'):
                print('Invalid input, continuing by default')


if __name__ == '__main__':
    load_dotenv()

    print('Welcome to Trip Planner Deluxe™')
    while True:
        location = input('\nEnter your destination, or press q to quit: ')
        if location == 'q':
            break
        print('Your travel information for ' + location + ':')

        # simple error handler, the get_weather function handles other error stuff inside its file
        try:
            weatherReport = get_weather(getenv("WEATHERAPI_KEY"), location)
            assert weatherReport is not False
        except AssertionError:
            continue

        # reuse the exact location that the weather api returns, making it easier to find locations in other api calls
        precise_location = f"{weatherReport.location['name']}, {weatherReport.location['region']}"
        latitude, longitude = weatherReport.location["lat"], weatherReport.location["lon"]
        # prints each location
        getWeather(weatherReport)
        getAttractions(latitude, longitude, precise_location)
        getFood(latitude, longitude, precise_location)
