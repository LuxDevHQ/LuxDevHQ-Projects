# World Bank Economic Indicators Pipeline

## Project Objective
Extract development indicators from the World Bank API for selected African countries, store them in PostgreSQL, and analyze development trends.

## API Used
World Bank API: `https://api.worldbank.org/`

## Indicator Codes
- Population: `SP.POP.TOTL`
- GDP: `NY.GDP.MKTP.CD`
- Inflation Rate: `FP.CPI.TOTL.ZG`
- Unemployment Rate: `SL.UEM.TOTL.ZS`
- Life Expectancy: `SP.DYN.LE00.IN`
- Access to Electricity: `EG.ELC.ACCS.ZS`

## Setup Steps
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run SQL in `database_setup.sql` to create database and table.
3. Update DB credentials in `extract_world_bank_data.py`.

## How to Run
```bash
python extract_world_bank_data.py
```

## Analysis Questions
- Which country has the latest highest GDP?
- How has Kenya's GDP changed over time?
- Which countries have better access to electricity?
- What is the average life expectancy by country?
