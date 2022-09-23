import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN_AUTH = '88e2b3b0fa04449dbc294fd54ce71bc4'
TOKEN = 'y0_AgAAAABku0RnAADLWwAAAADPYfxHu2RBKwDEQZqlxnjv2EPUE8NbTvc'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
FILE_TO_COPY = 'Файл для копирования.jpg'


def get_data(path):
    response = requests.get('{}?path={}'.format(URL, path), headers=headers)
    json = response.json()
    items_list = json["_embedded"]["items"]
    file_list = []
    for item in items_list:
        if item["type"] == 'file':
            file_list.append({
                'name': item["name"],
                'path': item["path"]
            })

    print(response.status_code)
    print(file_list)


def create_folder(path):
    """ create folder \n path """
    response = requests.put('{}?path={}'.format(URL, path), headers=headers)
    print(response.status_code, response.text)


def copy_file(file, path):
    """ copy file from root folder to /path """
    final_path = path + '/' + file
    response = requests.post('{}/copy?from=/{}&path=/{}'.format(URL, file, final_path), headers=headers)
    print(response.status_code, response.text)


def rename_file(old_name, new_name):
    """ rename file from old_name to new_name """
    response = requests.post('{}/move?from=/{}&path=/{}'.format(URL, old_name, new_name), headers=headers)
    print(response.status_code, response.text)


if __name__ == '__main__':
    pass
    # create_folder("Test")
    # copy_file(FILE_TO_COPY, "Test")
    # rename_file("Test/" + FILE_TO_COPY, "Test/" + "rename.jpg")
    # get_data("/Test")
    # get_token()
