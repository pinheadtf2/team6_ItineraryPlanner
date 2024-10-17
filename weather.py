import asyncio
from os import getenv

import aiohttp
from dotenv import load_dotenv


class Weather:
    def __init__(self,
                 location: tuple,
                 current_temperature: float,
                 max_temperature: float,
                 min_temperature: float,
                 condition: str,
                 daily_condition: str,
                 wind_speed: float,
                 precipitation_chance: int
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
        """
        self.location = location
        self.current_temperature = current_temperature
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.condition = condition
        self.daily_condition = daily_condition
        self.wind_speed = wind_speed
        self.precipitation_chance = precipitation_chance


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
            report = await response.json()
            current = report["current"]
            forecast = report["forecast"]["forecastday"][0]['day']
            if forecast["daily_chance_of_rain"] > forecast["daily_chance_of_snow"]:
                precipitation = forecast["daily_chance_of_rain"]
            else:
                precipitation = forecast["daily_chance_of_snow"]

            constructed_class = Weather(report["location"], current["temp_f"], forecast["maxtemp_f"],
                                        forecast["mintemp_f"], current["condition"]["text"],
                                        forecast["condition"]["text"], current["wind_mph"], precipitation)
            return constructed_class


def get_weather(location: str) -> Weather:
    """
    Helper function that loads the key and submits the request to the Weather API. Call this to get the weather.

    :param location: The location you want to get the weather for.
    :return: A class containing the current weather and forecast.
    """
    load_dotenv()
    response = asyncio.run(current_forecast_weather(getenv("WEATHERAPI_KEY"), location))
    print(response)
    return response


if __name__ == '__main__':
    get_weather("Menomonie")
