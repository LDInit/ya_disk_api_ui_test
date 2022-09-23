import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN_AUTH = '88e2b3b0fa04449dbc294fd54ce71bc4'
TOKEN = 'y0_AgAAAABku0RnAADLWwAAAADPYfxHu2RBKwDEQZqlxnjv2EPUE8NbTvc'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
FILE_TO_COPY = 'Файл для копирования.jpg'
NEW_FOLDER_NAME = 'Test'


def test_create_folder():
    """ create folder \n path """
    response = requests.put('{}?path={}'.format(URL, NEW_FOLDER_NAME), headers=headers)
    assert response.status_code == 201


def test_copy_file():
    """ copy file from root folder to /path """
    final_path = NEW_FOLDER_NAME + '/' + FILE_TO_COPY
    response = requests.post('{}/copy?from=/{}&path=/{}'.format(URL, FILE_TO_COPY, final_path), headers=headers)
    assert response.status_code == 201


def test_rename_file():
    """ rename file from old_name to new_name """
    old_path = NEW_FOLDER_NAME + '/' + FILE_TO_COPY
    new_path = NEW_FOLDER_NAME + '/updated_file.jpg'
    response = requests.post('{}/move?from=/{}&path=/{}'.format(URL, old_path, new_path), headers=headers)
    assert response.status_code == 201

