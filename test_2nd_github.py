import os
import time
import requests
from http.client import responses
from uuid import uuid4

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


#def test_create_repo():
#    repo_name = f"test-repo-{uuid4()}"
#    payload = {"name": repo_name, "private": True}
#    response = requests.post(f"{BASE_URI}/user/repos", headers=HEADERS, json=payload)
#    assert response.status_code == 201

#def test_delete_repo():
#    response = requests.delete(f"https://api.github.com/repos/justxki/test-repo-9f0607ad-5aa1-494b-b3e7-301ffb7f1289", headers=HEADERS)
#    assert response.status_code == 204

#def test_create_repo():
#    repo_name = f"test-playground"
#    payload = {"name": repo_name, "private": True}
#    response = requests.post(f"{BASE_URI}/user/repos", headers=HEADERS, json=payload)
#    assert response.status_code == 201












def test_create_issue():
    payload = {"title": "Bruh your repo suxx what's the deal?"} #forgot the word payload had to peak
    response = requests.post("https://api.github.com/repos/justxki/test-playground/issues", json=payload, headers=HEADERS)
    assert response.status_code == 201



def test_list_issues():
    response = requests.get(f"{BASE_URI}/repos/justxki/test-playground/issues", headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_and_close_issue():
    payload = {"title": "closeable test issue"}
    create_response = requests.post(f"{BASE_URI}/repos/justxki/test-playground/issues", headers=HEADERS, json=payload)
    print(create_response.json())  # <-- dump it
    assert create_response.status_code == 201
    issue_number = create_response.json()["number"]

    close_response = requests.patch(
        f"{BASE_URI}/repos/justxki/test-playground/issues/{issue_number}",
        headers=HEADERS,
        json={"state": "closed"}
    )
    assert close_response.status_code == 200































def test_create_and_close():
    payload = {"title": "new complaint"}
    create_response = requests.post(f"{BASE_URI}/repos/justxki/test-playground/issues", headers=HEADERS, json=payload)
    assert create_response.status_code == 201
    ticket_number = create_response.json()["number"]
    close_response = requests.patch(f"{BASE_URI}/repos/justxki/test-playground/issues/{ticket_number}",
                              headers=HEADERS, json={"state": "closed"})
    assert close_response.status_code == 200
    assert close_response.json()["state"] == "closed"



def test_unauthorized():
    response = requests.get(f"{BASE_URI}/user", headers=BAD_HEADERS)
    user_page = response.json()
    assert response.status_code == 401















def test_not_found_error_handling():
    response2 = requests.delete(f"{BASE_URI}/repos/justxki/REPO-THATLL-GET-ME-HIRED", headers=HEADERS)
    #print(responses2.json()["message"])
    assert response2.status_code == 404
    assert response2.json()["message"] == "Not Found"















def test_invalid_typo_value():
    payload = {"titles": "this aint a title bby girl"}
    response = requests.post(f"{BASE_URI}/repos/justxki/test-playground/issues", headers=HEADERS, json=payload)
    #print(response.json())
    assert response.status_code == 422
    #assert response.json()["message"] == 'Invalid request.\n\n"title" wasn\'t supplied.'
    assert "Invalid request" in response.json()["message"]





def test_error_malformed_json():
    response = requests.post(f"{BASE_URI}/repos/justxki/test-playground", headers=HEADERS)
    print(response.json())
    assert response.status_code == 400
    assert "JSON object" in response.json()["message"]

def test_error_create_dupe():
    payload = {"name": "test-playground"}
    response = requests.post(f"{BASE_URI}/user/repos", headers=HEADERS, json=payload)
    #print(response.json())
    assert response.status_code == 422 #409 adjacent
    #assert "Repository creation failed" in response.json()["message"]
    assert response.json()["errors"][0]["message"] == "name already exists on this account"


def test_somethin():
    payload = {"title": "fried"}
    response = requests.post(f"{BASE_URI}/repos/justxki/test-playground/issues", headers=HEADERS, json=payload)
    new_issue_number = response.json()["number"]

    # Poll up to 5 times, waiting 0.5 seconds between tries
    issue_found = False
    for _ in range(5):
        list_of_issues = requests.get(f"{BASE_URI}/repos/justxki/test-playground/issues?per_page=100", headers=HEADERS)
        if any(issue["number"] == new_issue_number for issue in list_of_issues.json()):
            issue_found = True
            break
        time.sleep(0.5)

    assert issue_found, f"Issue {new_issue_number} never appeared in the issues list"




















def test_verify_closed_shape():
    payload = {"title": "new issue"}
    response = requests.post(f"{ISSUES_URI}", headers=HEADERS, json=payload)
    issue_number = response.json()["number"]
    assert response.json()["state"] == "open"
    payload = {"state": "closed"}
    response2 = requests.patch(f"{ISSUES_URI}/{issue_number}", headers=HEADERS, json=payload)
    assert response2.json()["state"] == "closed"
    response3 = requests.get(f"{ISSUES_URI}/{issue_number}", headers=HEADERS, json=payload)
    assert response3.json()["state"] == "closed"





