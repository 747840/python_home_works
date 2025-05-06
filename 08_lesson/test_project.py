import requests
from ProjectsAPI import ProjectsAPI


api = ProjectsAPI("https://ru.yougile.com",
                  "9vF69iXCYF90HHl0cDduk1lzSSDzZNNVHyyt3aiax0BRZ"
                  "-Tq43GbXhTgyn4CombX")


# Создать новый проект
def test_post_projects_positive():
    # Получить колличество проектов
    body = api.get_project_list()
    len_before = len(body)
    assert len(body) > 0
    # Создать новый проект
    title = "Аврора"
    result = api.create_project(title)
    id = result['id']
    # Получить колличество проектов
    body = api.get_project_list()
    len_after = len(body)
    assert len(body) > 0
    # Проверить, что +1
    assert len_after - len_before == 1
    # Проверить название и ib последнего проекта
    assert body[-1]["title"] == "Аврора"
    assert body[-1]["id"] == id


# Создать проект без названия
def test_post_projects_negative():
    data = {
        "title": "",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    resp = requests.post(api.url + '/api-v2/projects',
                         json=data, headers=api.headers)
    assert resp.status_code == 400


# Изменить название проекта
def test_put_projects_positive():
    # Создать новый проект
    title = "Аврора"
    result = api.create_project(title)
    id = result['id']
    # Изменить название проекта
    data = {
        "title": "Ррорра",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    resp = requests.put(f'{api.url}/api-v2/projects/{id}',
                        json=data, headers=api.headers)
    assert resp.status_code == 200


def test_put_projects_negative():
    # Создать новый проект
    title = "Аврора"
    result = api.create_project(title)
    id = result['id']
    # Изменить название проекта, оставить пустым
    data = {
        "title": "",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    resp = requests.put(f'{api.url}/api-v2/projects/{id}',
                        json=data, headers=api.headers)
    assert resp.status_code == 400


def test_get_projects_positive():
    # Создать новый проект
    title = "Роза"
    result = api.create_project(title)
    id = result['id']
    # Получить проект по id
    resp = requests.get(f'{api.url}/api-v2/projects/{id}',
                        headers=api.headers)
    assert resp.status_code == 200


def test_get_projects_negative():
    resp = requests.get(api.url+'/api-v2/projects/123456789',
                        headers=api.headers)
    assert resp.status_code == 404
