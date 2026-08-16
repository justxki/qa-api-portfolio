import requests
from config import HEADERS, ISSUES_URI


class GithubClient:

    def __init__(self):
        self.headers = HEADERS
        self.issues_uri = ISSUES_URI


    def create_issue(self, title):
        payload = {"title": title}
        response = requests.post(self.issues_uri, headers=self.headers, json=payload)
        return response