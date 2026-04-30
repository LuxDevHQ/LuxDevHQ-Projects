CREATE DATABASE world_bank_db;

CREATE TABLE IF NOT EXISTS economic_indicators (
    indicator_id SERIAL PRIMARY KEY,
    country_name VARCHAR(100),
    country_code VARCHAR(10),
    indicator_name VARCHAR(200),
    indicator_code VARCHAR(50),
    year INTEGER,
    indicator_value NUMERIC,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
