from datetime import datetime
import requests
import psycopg2

DB_NAME = "world_bank_db"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

COUNTRIES = {
    "Kenya": "KEN", "Uganda": "UGA", "Tanzania": "TZA", "Rwanda": "RWA",
    "Ethiopia": "ETH", "Ghana": "GHA", "Nigeria": "NGA", "South Africa": "ZAF"
}

INDICATORS = {
    "Population": "SP.POP.TOTL",
    "GDP": "NY.GDP.MKTP.CD",
    "Inflation Rate": "FP.CPI.TOTL.ZG",
    "Unemployment Rate": "SL.UEM.TOTL.ZS",
    "Life Expectancy": "SP.DYN.LE00.IN",
    "Access to Electricity": "EG.ELC.ACCS.ZS",
}

def fetch_indicator_data(country_name, country_code, indicator_name, indicator_code):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}"
    params = {"format": "json", "per_page": 60}
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data[1] if isinstance(data, list) and len(data) > 1 else []
    except (requests.RequestException, ValueError) as exc:
        print(f"❌ Failed to fetch {indicator_name} for {country_name}: {exc}")
        return []

def clean_indicator_data(raw_data, country_name, country_code, indicator_name, indicator_code):
    records = []
    extracted_at = datetime.utcnow()
    for row in raw_data:
        value = row.get("value")
        year = row.get("date")
        if value is None or year is None:
            continue
        records.append({
            "country_name": country_name,
            "country_code": country_code,
            "indicator_name": indicator_name,
            "indicator_code": indicator_code,
            "year": int(year),
            "indicator_value": value,
            "extracted_at": extracted_at,
        })
    return records

def connect_to_database():
    try:
        return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    except psycopg2.Error as exc:
        print(f"❌ Database connection failed: {exc}")
        return None

def insert_indicator_records(records):
    if not records:
        print("⚠️ No indicator records to insert.")
        return
    conn = connect_to_database()
    if not conn:
        return
    query = """
    INSERT INTO economic_indicators (
        country_name, country_code, indicator_name, indicator_code,
        year, indicator_value, extracted_at
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    try:
        with conn.cursor() as cur:
            for r in records:
                cur.execute(query, (r["country_name"], r["country_code"], r["indicator_name"], r["indicator_code"], r["year"], r["indicator_value"], r["extracted_at"]))
        conn.commit()
        print(f"✅ Inserted {len(records)} economic indicator records.")
    except psycopg2.Error as exc:
        conn.rollback()
        print(f"❌ Failed to insert records: {exc}")
    finally:
        conn.close()

def main():
    all_records = []
    for country_name, country_code in COUNTRIES.items():
        for indicator_name, indicator_code in INDICATORS.items():
            raw_data = fetch_indicator_data(country_name, country_code, indicator_name, indicator_code)
            cleaned = clean_indicator_data(raw_data, country_name, country_code, indicator_name, indicator_code)
            all_records.extend(cleaned)
    insert_indicator_records(all_records)

if __name__ == "__main__":
    main()
