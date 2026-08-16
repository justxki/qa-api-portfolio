import requests
from uuid import uuid4
import os

from config import HEADERS, BASE_URI

def test_get_authenticated_user():
    response = requests.get(f"{BASE_URI}/user", headers=HEADERS)
    assert response.status_code == 200
    assert "login" in response.json()

def test_list_my_repos():
    response = requests.get(f"{BASE_URI}/user/repos", headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_and_delete_repo():
    repo_name = f"test-repo-{uuid4()}"
    payload = {"name": repo_name, "private": True}

    create_response = requests.post(f"{BASE_URI}/user/repos", headers=HEADERS, json=payload)
    assert create_response.status_code == 201

    delete_response = requests.delete(f"{BASE_URI}/repos/justxki/{repo_name}", headers=HEADERS)
    assert delete_response.status_code == 204