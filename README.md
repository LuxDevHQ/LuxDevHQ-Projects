# Python Data Extraction Projects

This repository contains beginner-friendly Python projects designed to help students practice core data engineering and automation skills, including:

- API extraction
- Web automation
- JSON processing
- CSV export
- PostgreSQL loading
- SQL analysis
- Basic data engineering workflows

## Projects in This Repository

### 1) Weather Data Pipeline Using Open-Meteo API
Students extract weather forecast data for Kenyan cities (Nairobi, Mombasa, Kisumu, Eldoret, and Nakuru), load it into PostgreSQL, and run SQL analysis queries.

- Folder: `weather_project/`
- Focus areas: API calls, data cleaning, PostgreSQL inserts, SQL reporting

### 2) World Bank Economic Indicators Pipeline
Students extract economic and development indicators for selected African countries using the World Bank API, store the data in PostgreSQL, and analyze trends.

- Folder: `world_bank_project/`
- Focus areas: looping over countries and indicators, missing-value handling, trend analysis

### 3) GitHub Repository Analytics Pipeline
Students extract public repository metrics from the GitHub REST API and analyze stars, forks, open issues, and programming languages.

- Folder: `github_analytics_project/`
- Focus areas: API authentication with optional token, rate-limit handling, repo analytics

### 4) Playwright Login and Data Extraction Project
Students automate login on a safe demo website and extract protected page details into CSV.

- Folder: `playwright_login_project/`
- Focus areas: browser automation, selector handling, extraction validation, CSV output

## Skills Students Will Learn

- Python functions
- API requests
- Working with JSON
- Lists and dictionaries
- Data cleaning
- Error handling
- PostgreSQL database connection
- SQL table creation
- SQL analysis queries
- Browser automation with Playwright
- Saving data to CSV
- Project documentation

## General Setup

```bash
git clone <repo-url>
cd python-data-extraction-projects
```

Each project has its own `requirements.txt`, so install dependencies inside each project folder.

## Recommended Learning Order

| Order | Project | Difficulty |
|---|---|---|
| 1 | Weather Data Pipeline | Beginner |
| 2 | World Bank Economic Indicators Pipeline | Beginner to Intermediate |
| 3 | GitHub Repository Analytics Pipeline | Intermediate |
| 4 | Playwright Login and Data Extraction | Intermediate |

## Database Note

PostgreSQL is required for the first three projects:

- `weather_project`
- `world_bank_project`
- `github_analytics_project`

Before running scripts, update database credentials inside each Python file.

## Ethics Note

Responsible data extraction matters:

- Respect website terms of service
- Do not scrape private systems without permission
- Do not overload APIs
- Use API keys safely
- Do not commit secrets to GitHub

## Deliverables

Each student should submit:

- Python scripts
- SQL files
- Screenshots of successful execution
- PostgreSQL tables with data
- Analysis query results
- README documentation
- Optional Power BI dashboard
