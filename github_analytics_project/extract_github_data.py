import os
from datetime import datetime
import requests
import psycopg2

DB_NAME = "github_analytics_db"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

REPOSITORIES = [
    "microsoft/vscode", "pandas-dev/pandas", "numpy/numpy", "django/django",
    "tensorflow/tensorflow", "apache/airflow", "scikit-learn/scikit-learn",
    "fastapi/fastapi", "psf/requests", "matplotlib/matplotlib",
]

def fetch_repository_data(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    try:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 403:
            print(f"⚠️ Rate limit reached while fetching {owner}/{repo}. Try again later or use GITHUB_TOKEN.")
            return None
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        print(f"❌ Failed fetching {owner}/{repo}: {exc}")
        return None

def clean_repository_data(raw_data):
    if not raw_data:
        return None
    return {
        "repo_name": raw_data.get("name"),
        "owner_name": raw_data.get("owner", {}).get("login"),
        "description": raw_data.get("description") or "No description provided",
        "programming_language": raw_data.get("language") or "Not specified",
        "stars": raw_data.get("stargazers_count", 0),
        "forks": raw_data.get("forks_count", 0),
        "open_issues": raw_data.get("open_issues_count", 0),
        "watchers": raw_data.get("watchers_count", 0),
        "created_at": raw_data.get("created_at"),
        "updated_at": raw_data.get("updated_at"),
        "repo_url": raw_data.get("html_url"),
        "extracted_at": datetime.utcnow(),
    }

def connect_to_database():
    try:
        return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    except psycopg2.Error as exc:
        print(f"❌ Database connection failed: {exc}")
        return None

def insert_repository_records(records):
    conn = connect_to_database()
    if not conn:
        return
    query = """
    INSERT INTO github_repositories (
        repo_name, owner_name, description, programming_language, stars,
        forks, open_issues, watchers, created_at, updated_at, repo_url, extracted_at
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        with conn.cursor() as cur:
            for r in records:
                cur.execute(query, (r["repo_name"], r["owner_name"], r["description"], r["programming_language"], r["stars"], r["forks"], r["open_issues"], r["watchers"], r["created_at"], r["updated_at"], r["repo_url"], r["extracted_at"]))
        conn.commit()
        print(f"✅ Inserted {len(records)} repository records.")
    except psycopg2.Error as exc:
        conn.rollback()
        print(f"❌ Failed to insert records: {exc}")
    finally:
        conn.close()

def main():
    records = []
    for full_name in REPOSITORIES:
        owner, repo = full_name.split("/")
        raw = fetch_repository_data(owner, repo)
        cleaned = clean_repository_data(raw)
        if cleaned:
            records.append(cleaned)
    if records:
        insert_repository_records(records)
    else:
        print("⚠️ No repository data collected.")

if __name__ == "__main__":
    main()
