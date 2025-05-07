import requests


class ProjectsAPI:

    def __init__(self, url, key):
        self.url = url
        self.key = \
            "9vF69iXCYF90HHl0cDduk1lzSSDzZNNVHyyt3aiax0BRZ-Tq43GbXhTgyn4CombX"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

    def get_project_list(self):
        resp = requests.get(self.url + '/api-v2/projects',
                            headers=self.headers)
        return resp.json().get("content", [])

    def create_project(self, title=""):
        data = {
            "title": title,
            "users": {
                "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
            }
        }
        resp = requests.post(self.url + '/api-v2/projects',
                             json=data, headers=self.headers)
        return resp.json()
