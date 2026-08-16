import pytest
from clients.github_client import GithubClient

@pytest.fixture
def github():
    return GithubClient()

def test_create_issue(github):
    response = github.create_issue("Test Title Name")
    assert response.status_code == 201
    assert response.json()["title"] == "Test Title Name"
    assert response.json()["state"] == "open"
    assert response.json()["number"] > 0

def test_close_issue(github):
    response = github.create_issue("Test Title Name")
    ticket_num = response.json()["number"]
    response2 = github.close_issue(ticket_num)
    assert response2.status_code == 200
    assert response2.json()["state"] == "closed"
