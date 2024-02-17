import json

import pytest

from config import DATA_TEST
from src.GetAPIHH import GetAPIHH
from src.JsonSave import JsonSave


@pytest.fixture
def fixture_class_get_hh_valid():
    return GetAPIHH().get_vacancy_from_api('python')


@pytest.fixture
def fixture_class_get_hh_negative():
    return GetAPIHH().get_vacancy_from_api("1")


@pytest.fixture
def fixture_class_json_saver():
    return JsonSave()


@pytest.fixture
def fixture_class_list():
    json_saver = JsonSave()
    json_saver.save_file([{'name': 'Roman'}])
    return json_saver


@pytest.fixture
def new_file():
    with open(DATA_TEST, encoding='utf-8') as file:
        return json.load(file)
