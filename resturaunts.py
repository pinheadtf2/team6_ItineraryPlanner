import requests


def find_nearby_restaurants(api_key, latitude, longitude, radius=1000):
    # Define the API URL for nearby search
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&type=restaurant&key={api_key}"

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
