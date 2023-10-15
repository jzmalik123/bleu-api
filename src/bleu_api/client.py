import requests


class BleuAPIClient:

    BASE_URL = "https://sdk.faceki.com"
    # CLIENT_ID = "4mfq2291m54gtg4t50gh83bcaa"
    # CLIENT_SECRET = "5uo8j2pq1dfmsmirkoim6rmse3og78ee0el86eltd6oh96fi3ao"

    def __init__(self, client_id, client_secret):
        self.base_url = BleuAPIClient.BASE_URL
        self.client_id = client_id
        self.client_secret = client_secret

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
