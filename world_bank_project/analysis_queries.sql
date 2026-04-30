-- Latest GDP by country
SELECT DISTINCT ON (country_name) country_name, year, indicator_value AS latest_gdp
FROM economic_indicators
WHERE indicator_name = 'GDP'
ORDER BY country_name, year DESC;

-- Latest population by country
SELECT DISTINCT ON (country_name) country_name, year, indicator_value AS latest_population
FROM economic_indicators
WHERE indicator_name = 'Population'
ORDER BY country_name, year DESC;

-- Kenya GDP trend over time
SELECT year, indicator_value AS gdp
FROM economic_indicators
WHERE country_name = 'Kenya' AND indicator_name = 'GDP'
ORDER BY year;

-- Access to electricity by country
SELECT country_name, year, indicator_value AS electricity_access
FROM economic_indicators
WHERE indicator_name = 'Access to Electricity'
ORDER BY country_name, year DESC;

-- Indicators with missing or low values
SELECT country_name, indicator_name, year, indicator_value
FROM economic_indicators
WHERE indicator_value IS NULL OR indicator_value < 1
ORDER BY country_name, indicator_name, year DESC;

-- Average life expectancy by country
SELECT country_name, ROUND(AVG(indicator_value), 2) AS avg_life_expectancy
FROM economic_indicators
WHERE indicator_name = 'Life Expectancy'
GROUP BY country_name
ORDER BY avg_life_expectancy DESC;
