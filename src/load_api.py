import json

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
        self.endpoint = f'employers'
        self.keyword = keyword
        self.params = {'text': self.keyword, 'only_with_vacancies': True, 'per_page': 5}

        self.response = requests.get(f'{self.url}{self.endpoint}', params=self.params)

    def get_info_via_API(self):
        self.response = self.response.json()
        return self.response

    def get_id_employer(self):
        self.all_id = []
        for employer_id in self.response['items']:
            self.all_id.append(employer_id['id'])
            if len(self.all_id) == 9:
                break

        return self.all_id

    def get_info_via_id(self, id):

        self.id = id

        endpoint = f'vacancies?employer_id={self.id}'
        params = {'per_page': 10, 'page': 1}

        response = requests.get(f'{self.url}{endpoint}', params=params)
        self.final = response.json()
        return self.final

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
hh_api.get_info_via_API()
hh_api.get_id_employer()
all_items = []
print(hh_api.all_id)
for id in hh_api.all_id:
    hh_api.get_info_via_id(id)
    data_hh = hh_api.final
    all_items.append(data_hh)

merged_items = []
for json_data in all_items:
    merged_items.extend(json_data.get('items', []))



with open("json.json", "w", encoding='utf-8') as json_file:
    for item in merged_items:
        json.dump(item, json_file, ensure_ascii=False)
        json_file.write('\n')

# print(merged_json)


# data_hh = hh_api.final

# print(data_hh)
