# GitHub Repository Analytics Pipeline

## Project Objective
Extract public repository metadata from GitHub REST API, load it into PostgreSQL, and analyze repository popularity.

## How GitHub API Extraction Works
The script loops through a fixed list of repositories, fetches each repository profile from `https://api.github.com/repos/{owner}/{repo}`, cleans missing values, and stores the result in PostgreSQL.

## Optional GitHub Token Setup
Set an optional token to increase rate limits:

```bash
export GITHUB_TOKEN="your_token_here"
```

## Database Setup
1. Run `database_setup.sql` in PostgreSQL.
2. Update database credentials in `extract_github_data.py`.

## Run the Script
```bash
python extract_github_data.py
```

## Analysis Questions
- Which repository has the most stars?
- Which repository has the most forks?
- Which programming languages appear most often?
- Which repositories have the most open issues?
- Which repositories were updated recently?
