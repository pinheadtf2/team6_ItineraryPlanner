import requests


def find_nearby_restaurants(api_key, location, radius=1000, type='restaurant'):
    # Define the API URL for nearby search
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&key={api_key}"

    # Make the request to Google Places API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        restaurants = data.get('results', [])

        # Create a list to store restaurant details
        restaurant_list = []
        for place in restaurants:
            restaurant = {
                'name': place['name'],
                'rating': place.get('rating', 'N/A'),
                'address': place['vicinity']
            }
            restaurant_list.append(restaurant)

        # Return the list of restaurants
        return restaurant_list
    else:
        print("Error fetching data from Google Places API")
        return []


# Prompt user for API key and location
api_key = input("Please enter your Google API key: ")
latitude = input("Please enter the latitude: ")
longitude = input("Please enter the longitude: ")

# Combine latitude and longitude into one string
location = f"{latitude},{longitude}"

# Call the function to get the restaurant data
restaurants = find_nearby_restaurants(api_key, location)

# Print the list of nearby restaurants
if restaurants:
    for r in restaurants:
        print(r)
else:
    print("No restaurants found.")

