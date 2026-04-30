CREATE DATABASE weather_db;

CREATE TABLE IF NOT EXISTS weather_data (
    weather_id SERIAL PRIMARY KEY,
    city_name VARCHAR(100),
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6),
    weather_date DATE,
    temperature DECIMAL(10, 2),
    rainfall DECIMAL(10, 2),
    wind_speed DECIMAL(10, 2),
    humidity DECIMAL(10, 2),
    weather_condition VARCHAR(100),
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
