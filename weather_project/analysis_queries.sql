-- Highest temperature by city
SELECT city_name, MAX(temperature) AS highest_temperature
FROM weather_data
GROUP BY city_name
ORDER BY highest_temperature DESC;

-- Highest rainfall by city
SELECT city_name, MAX(rainfall) AS highest_rainfall
FROM weather_data
GROUP BY city_name
ORDER BY highest_rainfall DESC;

-- Average temperature per city
SELECT city_name, ROUND(AVG(temperature), 2) AS average_temperature
FROM weather_data
GROUP BY city_name
ORDER BY average_temperature DESC;

-- Highest wind speed by city
SELECT city_name, MAX(wind_speed) AS highest_wind_speed
FROM weather_data
GROUP BY city_name
ORDER BY highest_wind_speed DESC;

-- Total records extracted per city
SELECT city_name, COUNT(*) AS total_records
FROM weather_data
GROUP BY city_name
ORDER BY total_records DESC;
