from weather import get_weather

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


def getAttractions(loc):
    print('===========================================')
    print('Things to do around ' + loc + ':\n')
    for att in tempAttrac:
        print('Name: ' + att[0])
        print('Rating: ' + att[1])
        print('Address: ' + att[2] + '\n')


def getFood(loc):
    print('===========================================')
    print('Places to eat in ' + loc + ':\n')
    for att in tempAttrac:
        print('Name: ' + att[0])
        print('Rating: ' + att[1])
        print('Address: ' + att[2] + '\n')


print('Welcome to Trip Planner Deluxe™')
while True:
    location = input('\nEnter your destination, or press q to quit: ')
    if location == 'q':
        break
    print('Your travel information for ' + location + ':')

    # simple error handler, the get_weather function handles other error stuff inside its file
    try:
        weatherReport = get_weather(location)
        assert weatherReport is not False
    except AssertionError:
        continue

    # reuse the exact location that the weather api returns, making it easier to find locations in other api calls
    precise_location = f"{weatherReport.location['name']}, {weatherReport.location['region']}"

    # prints each location
    getWeather(weatherReport)
    # getAttractions(precise_location)
    # getFood(precise_location)
