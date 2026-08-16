import requests
HEADERS = {"Authorization": f"Bearer YOUR_TOKEN", "Accept": "application/vnd.github+json"}
BASE_URI = "https://api.github.com"

response = requests.get(f"{BASE_URI}/repos/justxki/test-playground/issues?state=open&per_page=100", headers=HEADERS)
for issue in response.json():
    requests.patch(f"{BASE_URI}/repos/justxki/test-playground/issues/{issue['number']}", headers=HEADERS, json={"state": "closed"})
    print(f"closed #{issue['number']}")