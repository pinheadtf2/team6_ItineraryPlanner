import requests


def get_nearby_attractions(api_key, latitude, longitude, radius=1000, place_type='tourist_attraction'):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f"{latitude},{longitude}",
        'radius': radius,
        'type': place_type,
        'key': api_key
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        results = response.json().get('results', [])
        attractions = []
        for place in results:
            name = place.get('name')
            address = place.get('vicinity')
            rating = place.get('rating')
            attractions.append({
                'name': name,
                'address': address,
                'rating': rating
            })
        return attractions
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []


def main():
    # User input
    print("Welcome to the Nearby Attractions Finder!")
    api_key = input("Enter your Google Places API key: ")
    latitude = float(input("Enter the latitude of the location: "))
    longitude = float(input("Enter the longitude of the location: "))
    radius = int(input("Enter the search radius in meters (e.g., 2000 for 2 km): "))

    # Fetch and display nearby attractions
    attractions = get_nearby_attractions(api_key, latitude, longitude, radius)

    if attractions:
        print("\nNearby Attractions:")
        for i, attraction in enumerate(attractions, 1):
            print(f"{i}. {attraction['name']} - {attraction['address']} (Rating: {attraction.get('rating', 'N/A')})")
    else:
        print("No attractions found or there was an error with the request.")


if __name__ == "__main__":
    main()