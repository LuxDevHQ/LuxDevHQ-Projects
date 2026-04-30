"""Weather data extraction pipeline using Open-Meteo API.

This script fetches daily weather forecast data for selected Kenyan cities,
cleans the response, and inserts the records into PostgreSQL.
"""

from datetime import datetime
import requests
import psycopg2

DB_NAME = "weather_db"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

CITIES = {
    "Nairobi": (-1.286389, 36.817223),
    "Mombasa": (-4.043477, 39.668206),
    "Kisumu": (-0.091702, 34.767956),
    "Eldoret": (0.514277, 35.269779),
    "Nakuru": (-0.303099, 36.080025),
}

WEATHER_CODE_MAP = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog", 51: "Light drizzle", 53: "Drizzle",
    55: "Dense drizzle", 61: "Slight rain", 63: "Rain", 65: "Heavy rain",
    71: "Slight snow", 80: "Rain showers", 95: "Thunderstorm",
}


def get_weather_data(city_name, latitude, longitude):
    """Fetch weather forecast from Open-Meteo API for one city."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,precipitation_sum,wind_speed_10m_max,relative_humidity_2m_mean,weather_code",
        "timezone": "auto",
        "forecast_days": 7,
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        print(f"✅ API call successful for {city_name}.")
        return response.json()
    except requests.RequestException as exc:
        print(f"❌ Failed to fetch weather data for {city_name}: {exc}")
        return None


def clean_weather_data(raw_data, city_name, latitude, longitude):
    """Transform raw API JSON into a list of clean records."""
    records = []
    if not raw_data or "daily" not in raw_data:
        print(f"⚠️ No daily data found for {city_name}.")
        return records

    daily = raw_data["daily"]
    extracted_at = datetime.utcnow()

    for i, weather_date in enumerate(daily.get("time", [])):
        weather_code = daily.get("weather_code", [None] * len(daily.get("time", [])))[i]
        record = {
            "city_name": city_name,
            "latitude": latitude,
            "longitude": longitude,
            "weather_date": weather_date,
            "temperature": daily.get("temperature_2m_max", [None])[i],
            "rainfall": daily.get("precipitation_sum", [None])[i],
            "wind_speed": daily.get("wind_speed_10m_max", [None])[i],
            "humidity": daily.get("relative_humidity_2m_mean", [None])[i],
            "weather_condition": WEATHER_CODE_MAP.get(weather_code, f"Code {weather_code}"),
            "extracted_at": extracted_at,
        }
        records.append(record)

    return records


def connect_to_database():
    """Create and return a PostgreSQL database connection."""
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        print("✅ Connected to PostgreSQL successfully.")
        return connection
    except psycopg2.Error as exc:
        print(f"❌ Database connection failed: {exc}")
        return None


def insert_weather_records(records):
    """Insert cleaned weather records into weather_data table."""
    if not records:
        print("⚠️ No records to insert.")
        return

    connection = connect_to_database()
    if not connection:
        return

    query = """
        INSERT INTO weather_data (
            city_name, latitude, longitude, weather_date, temperature,
            rainfall, wind_speed, humidity, weather_condition, extracted_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        with connection.cursor() as cursor:
            for record in records:
                cursor.execute(
                    query,
                    (
                        record["city_name"], record["latitude"], record["longitude"],
                        record["weather_date"], record["temperature"], record["rainfall"],
                        record["wind_speed"], record["humidity"], record["weather_condition"],
                        record["extracted_at"],
                    ),
                )
        connection.commit()
        print(f"✅ Inserted {len(records)} weather records.")
    except psycopg2.Error as exc:
        connection.rollback()
        print(f"❌ Failed to insert weather records: {exc}")
    finally:
        connection.close()


def main():
    """Run complete extraction process for all cities."""
    all_records = []
    for city_name, (latitude, longitude) in CITIES.items():
        raw_data = get_weather_data(city_name, latitude, longitude)
        records = clean_weather_data(raw_data, city_name, latitude, longitude)
        all_records.extend(records)

    insert_weather_records(all_records)


if __name__ == "__main__":
    main()
