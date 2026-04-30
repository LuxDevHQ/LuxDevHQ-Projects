# Playwright Login and Data Extraction Project

## Project Objective
Use Playwright to automate login on a safe demo website, navigate to the post-login page, extract key data fields, and save the result to CSV.

## Why Playwright Is Useful
Playwright helps automate browser tasks like form filling, login testing, navigation, and data extraction from dynamic pages.

## Installation Steps
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install Playwright browsers:
   ```bash
   playwright install
   ```

## How to Run
```bash
python login_extract.py
```

## Extracted Data
- Page title
- Current page URL
- Success message
- Full page text
- Extracted timestamp

## Important Ethical Note
Only use Playwright automation on demo websites, websites you own, or websites where you have permission to automate login and extract data.
