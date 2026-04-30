-- Repository with the most stars
SELECT repo_name, stars
FROM github_repositories
ORDER BY stars DESC
LIMIT 1;

-- Repository with the most forks
SELECT repo_name, forks
FROM github_repositories
ORDER BY forks DESC
LIMIT 1;

-- Most common programming languages
SELECT programming_language, COUNT(*) AS repository_count
FROM github_repositories
GROUP BY programming_language
ORDER BY repository_count DESC;

-- Repositories with the most open issues
SELECT repo_name, open_issues
FROM github_repositories
ORDER BY open_issues DESC;

-- Recently updated repositories
SELECT repo_name, updated_at
FROM github_repositories
ORDER BY updated_at DESC;

-- Average stars by programming language
SELECT programming_language, ROUND(AVG(stars), 2) AS average_stars
FROM github_repositories
GROUP BY programming_language
ORDER BY average_stars DESC;
