from clients.github_client import GithubClient

def test_create_issue():
    github = GithubClient()
    response = github.create_issue("Test Title Name")
    assert response.status_code == 201
    assert response.json()["title"] == "Test Title Name"
    assert response.json()["state"] == "open"
    assert response.json()["number"] > 0
