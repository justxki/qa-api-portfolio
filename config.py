import os

BASE_URI = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
BAD_HEADERS = {"Authorization": "Bearer fake_token_lol", "Accept": "application/vnd.github+json"}
OWNER = "justxki"
REPO_NAME = "test-playground"
REPO_URI = f"{BASE_URI}/repos/{OWNER}/{REPO_NAME}"
ISSUES_URI = f"{REPO_URI}/issues"
USER_URI = f"{BASE_URI}/user"
USER_REPOS_URI = f"{USER_URI}/repos"