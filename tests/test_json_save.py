from abc import ABC

from src.AbstractJsonSave import AbstractJsonSave
from src.JsonSave import JsonSave


def test_json_saver_issubclass():
    assert issubclass(JsonSave, AbstractJsonSave)
    assert issubclass(AbstractJsonSave, ABC)


def test_save_file_read_file(fixture_class_json_saver):
    fixture_class_json_saver.save_file([{'name': 'Roman'}])

    assert isinstance(fixture_class_json_saver.read_file(), list)
    assert fixture_class_json_saver.read_file() == [{'name': 'Roman'}]


def test_add_vacancy_to_file_and_delete(fixture_class_list):
    fixture_class_list.add_vacancy_to_file([{'name': 'Not Roman'}])

    assert fixture_class_list.read_file() == [{'name': 'Not Roman'}, {'name': 'Roman'}]

    fixture_class_list.delete_vacancy('Roman')
    assert fixture_class_list.read_file() == [{'name': 'Not Roman'}]