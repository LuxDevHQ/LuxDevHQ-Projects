### **Crypto Market Data Pipeline using CoinPaprika API, Python, PostgreSQL, and Power BI**

#### Objective

You are required to build a simple data pipeline that extracts cryptocurrency market data from the CoinPaprika API, processes it using Python, loads it into PostgreSQL, handles duplicate records, and prepares the data for SQL analysis and Power BI visualization.

---

### Tools Required

You will use:

- Python
- PostgreSQL
- DBeaver or pgAdmin
- Power BI
- CoinPaprika API

Required Python libraries:

- requests
- pandas
- psycopg2-binary

---

### Project Instructions

#### Step 1: Set Up Your Project Folder

#### Step 2: Install the Required Python Libraries

Install the Python libraries needed for the project.

**The libraries should allow you to:**

- Connect to an API
- Convert API data into a table format
- Connect Python to PostgreSQL

#### Step 3: Create a PostgreSQL Database.
- Create a new PostgreSQL database for storing cryptocurrency market data.

#### Step 4: Create a Table for Storing Crypto Market Data.

Create a table that can store the following information:

- Coin ID
- Coin name
- Coin symbol
- Coin rank
- Price in USD
- Market capitalization
- 24-hour trading volume
- 24-hour percentage price change
- Last updated time
I- nserted time

The table should also have a primary key.

#### Step 5: Identify the API Endpoint.

Use the CoinPaprika REST API to extract cryptocurrency ticker data.

You should extract data for at least four cryptocurrencies, for example:

- Bitcoin
- Ethereum
- Solana
- BNB

#### Step 6: Extract Data Using Python.

Write a Python script that connects to the CoinPaprika API and extracts crypto market data.

**Your script should:**
- Connect to the API endpoint
- Fetch data for selected cryptocurrencies
- Check whether the API request was successful
- Store the extracted data temporarily in Python

#### Step 7: Transform the Extracted Data.

Transform the API response into a clean tabular format. Your transformed data should include only the required fields listed in Step 4.

- Make sure the data is ready to be inserted into PostgreSQL.
  
#### Step 8: Connect Python to PostgreSQL. 

Update your Python script so that it connects to the PostgreSQL database.

**Your connection should include:**
- Host
- Database name
- Username
- Password
- Port


#### Step 9: Load the Data into PostgreSQL.

Insert the transformed crypto data into the PostgreSQL table. Your script should be able to load multiple cryptocurrency records into the database.

#### Step 10: Handle Duplicate Records.

Because the script can be run many times, duplicate records may be inserted.

**You are required to:**
- Create a way to check for duplicate records
- Create a way to prevent duplicate records
- Create a stored procedure that removes duplicate records

Duplicates should be checked based on a meaningful combination of fields such as:
- Coin ID
- Last updated time

#### Step 11: Test Duplicate Handling.

Run your Python script more than once. Then confirm whether duplicate records were inserted or prevented. Document what happened in your README file.

#### Step 12: Write SQL Analysis Queries.

Create SQL queries to answer the following business questions:
- Which cryptocurrency has the highest market capitalization?
- Which cryptocurrency has the highest 24-hour trading volume?
- Which cryptocurrency has the highest 24-hour percentage gain?
- Which cryptocurrency has the lowest price?
- How many records are stored in the table?
- Are there any duplicate records?
- What is the latest price for each cryptocurrency?

#### Step 13: Connect Power BI to PostgreSQL.

Connect Power BI to your PostgreSQL database. Use the crypto market data table as your data source.

#### Step 14: Build a Power BI Dashboard.

**Create a simple dashboard that shows:**
- Total number of cryptocurrencies
- Average price
- Market capitalization by cryptocurrency
- 24-hour trading volume by cryptocurrency
- 24-hour percentage price change
- Latest price table

**Use suitable visuals such as:**
- Cards
- Bar charts
- Column charts
- Tables
- Line charts
