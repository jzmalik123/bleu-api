import requests


class BleuAPIClient:

    BASE_URL = "https://api.example.com"
    CLIENT_ID = "your_api_key"
    CLIENT_SECRET = "your_client_secret"

    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint, method='GET', params=None, data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == 'GET':
                response = requests.get(url, params=params, headers=headers)
            elif method == 'POST':
                response = requests.post(url, data=data, headers=headers)
            # Add support for other HTTP methods as needed

            response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
            return response.json() if 'application/json' in response.headers.get('content-type',
                                                                                 '').lower() else response.text
        except requests.exceptions.RequestException as e:
            # Handle request errors here
            print(f"Request error: {e}")
            return None
