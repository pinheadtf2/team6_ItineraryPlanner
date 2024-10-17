#tempWeather = ()
att1 = ('name', 'rating', 'addr')
att2 = ('name', 'rating', 'addr')
att3 = ('name', 'rating', 'addr')
tempAttrac = (att1, att2, att3)

def getWeather(loc):
    print('===========================================')
    print('Weather for ' + loc + ':')

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
    location = input('Enter your destination, or press q to quit: ')
    if location == 'q':
        break
    print('Your travel information for ' + location + ':')
    getWeather(location)
    getAttractions(location)
    getFood(location)