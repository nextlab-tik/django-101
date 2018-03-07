def weather_status_logo(status):
    WEATHER_LOGOS = {
        "hot": "hot.png",
        "sunny": "sunny.png",
        "mostly sunny": "sunny.png",
        "thunderstorms":"thunderstorms.png",
        "severe thunderstorms":"thunderstorms.png",
        "scattered thunderstorms":" rain_s_cloudy.png",
        "partly cloudy": "partly_cloudy.png",
        "mostly cloudy": "partly_cloudy.png",
        "cloudy": "cloudy.png",
        "showers":"rain_light.png",
        "scattered showers":"rain_light.png",
        "rain": "rain.png",
        "snow":"snow.png",
        "heavy snow":"snow.png",
        "snow flurries":"snow.png",
        "blowing snow":"snow.png",
        "sleet":"sleet.png",
        "windy":"windy.png",
    }
    return "weather/" + WEATHER_LOGOS.get(status.lower(), "cloudy.png")
