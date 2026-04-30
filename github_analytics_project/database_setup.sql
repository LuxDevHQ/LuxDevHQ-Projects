CREATE DATABASE github_analytics_db;

CREATE TABLE IF NOT EXISTS github_repositories (
    repo_id SERIAL PRIMARY KEY,
    repo_name VARCHAR(200),
    owner_name VARCHAR(100),
    description TEXT,
    programming_language VARCHAR(100),
    stars INTEGER,
    forks INTEGER,
    open_issues INTEGER,
    watchers INTEGER,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    repo_url TEXT,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
