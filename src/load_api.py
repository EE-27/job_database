import requests


class HeadHunter_API:
    """
    API loader for HeadHunter job vacancies.
    """

    def __init__(self, keyword):
        """
        Initialize the HeadHunter API loader.

        Args: keyword (str): The keyword to search for in job vacancies.
        """
        self.data = None
        self.url = 'https://api.hh.ru/'
        self.endpoint = 'vacancies'
        self.keyword = keyword
        self.params = {'text': self.keyword}

        self.response = requests.get(f'{self.url}{self.endpoint}', params=self.params)

    def load(self):
        """
        Load data from the HeadHunter API.

        Returns: dict or str: The loaded data from the API if successful, or an error message if the request fails.
        """
        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data
        else:
            return f"Error when requesting data. Status code: {self.response.status_code}"

def loading(api):
    """
    Load data from the specified API.

    Args: api (LoadApi): An instance of a class that implements the LoadApi interface.

    Returns: dict or str: The loaded data from the API if successful, or an error message if the request fails.
    """
    api.load()
# Яндекс
keyword = "Яндекс"

hh_api = HeadHunter_API(keyword)

loading(hh_api)

data_hh = hh_api.data

print(data_hh)