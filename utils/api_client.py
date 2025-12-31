import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str, params=None):
        return requests.get(
            f"{self.base_url}{endpoint}",
            params=params
        )

    def post(self, endpoint: str, data=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            data=data
        )
