# Weather Data Pipeline Using Open-Meteo API

## Project Objective
Build a beginner-friendly data pipeline that extracts weather forecast data for selected Kenyan cities, stores the data in PostgreSQL, and runs SQL analysis queries.

## Tools Used
- Python
- Open-Meteo API
- PostgreSQL
- `requests`, `psycopg2-binary`, `pandas`

## Setup Steps
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure PostgreSQL is running.
4. Open `database_setup.sql` and run it in PostgreSQL.
5. Update database credentials in `extract_weather_data.py`.

## How to Create the Database
Run the SQL in `database_setup.sql` using `psql` or pgAdmin.

## How to Run the Script
```bash
python extract_weather_data.py
```

## Example Analysis Questions
- Which city had the highest recorded temperature?
- Which city had the highest rainfall?
- What is the average temperature by city?
- Which city had the strongest wind speed?
- How many records were extracted per city?
