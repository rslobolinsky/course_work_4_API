import json
from typing import Any

import requests

from src.AbstractGetAPIHH import AbstractGetAPIHH


class GetAPIHH(AbstractGetAPIHH):

    def __init__(self):
        self.all_vacancy = []

    def __repr__(self):
        return f"{self.all_vacancy}"

    def get_vacancy_from_api(self, name_vacancy) -> str | Any:
        """Get valid info about vacancies for user"""

        if name_vacancy.isalpha():
            keys_response = {'text': f'NAME:{name_vacancy}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            self.all_vacancy = json.loads(info.text)['items']
            return self.all_vacancy
        else:
            return "Vacancy not found"
