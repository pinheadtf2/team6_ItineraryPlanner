import asyncio

import aiohttp


class Weather:
    def __init__(self,
                 location: dict,
                 current_temperature: float,
                 max_temperature: float,
                 min_temperature: float,
                 condition: str,
                 daily_condition: str,
                 wind_speed: float,
                 precipitation_chance: int,
                 precipitation_type: str
                 ):
        """
        This represents the combined current and forecast as one class to make it easier when using the retrieved data.

        :param location: A tuple describing the returned location.
        :param current_temperature: The current temperature as a float, in real time.
        :param max_temperature: The day's maximum temperature as a float.
        :param min_temperature: The day's minimum temperature as a float.
        :param condition: The current condition at the location, in real time.
        :param daily_condition: The overall condition for the full day.
        :param wind_speed: The current wind speed as a float.
        :param precipitation_chance: The current chance of precipitation as a 0-100 integer.
        :param precipitation_type: The precipitation type as a string.
        """
        self.location = location
        self.current_temperature = current_temperature
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.condition = condition
        self.daily_condition = daily_condition
        self.wind_speed = wind_speed
        self.precipitation_chance = precipitation_chance
        self.precipitation_type = precipitation_type


async def current_forecast_weather(key: str, location: str) -> Weather:
    """
    This function is used to asynchronously retrieve the current weather forecast for a given location.
    :param key: The API key used to retrieve the weather forecast.
    :param location: The location you want to get the weather for.
    :return: A class containing the current weather and forecast.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.weatherapi.com/v1/forecast.json',
                               params={"key": key,
                                       "q": location
                                       }) as response:
            if response.status != 200:
                error = await response.json()
                if error["error"]["code"] == 1006:
                    raise ValueError("The location entered wasn't found. Please enter a valid location.")
                raise Exception(f"Status: {response.status}\nHeaders: {response.headers}\nResponse: {await response.json()}")

            report = await response.json()
            current = report["current"]
            forecast = report["forecast"]["forecastday"][0]['day']
            if forecast["daily_chance_of_rain"] > forecast["daily_chance_of_snow"]:
                precipitation = forecast["daily_chance_of_rain"]
                precip_type = "rain"
            else:
                precipitation = forecast["daily_chance_of_snow"]
                precip_type = "snow"

            constructed_class = Weather(report["location"], current["temp_f"], forecast["maxtemp_f"],
                                        forecast["mintemp_f"], current["condition"]["text"],
                                        forecast["condition"]["text"], current["wind_mph"], precipitation, precip_type)
            return constructed_class


def get_weather(key: str, location: str) -> Weather | bool:
    """
    Helper function that loads the key and submits the request to the Weather API. Call this to get the weather.

    :param location: The location you want to get the weather for.
    :return: A class containing the current weather and forecast.
    """
    try:
        if location == "Menomonie":
            print("Daring today, are we? \n")

        if len(location) < 3:
            raise ValueError("The location entered wasn't found. Please enter a valid location.")

        response = asyncio.run(current_forecast_weather(key, location))
        return response
    except ValueError as exception:
        print(exception)
        return False
    except Exception as exception:
        print(f"Could not get current weather!\n{exception}")
        return False
