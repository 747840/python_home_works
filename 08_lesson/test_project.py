import requests

base_url = "https://ru.yougile.com"


def test_post_projects_positive():
    # Получить колличество проектов
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.get(base_url + '/api-v2/projects', headers=headers)
    body = resp.json().get("content", [])
    len_before = len(body)
    assert resp.status_code == 200
    assert len(body) > 0
    # Создать новый проект
    data = {
        "title": "Аврора",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.post(base_url + '/api-v2/projects',
                         json=data, headers=headers)
    assert resp.status_code == 201
    new_id = resp.json()['id']

    # Получить колличество проектов
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.get(base_url + '/api-v2/projects', headers=headers)
    body = resp.json().get("content", [])
    len_after = len(body)
    assert resp.status_code == 200
    assert len(body) > 0
    # Проверить, что +1
    assert len_after - len_before == 1
    # Проверить название и ib последнего проекта
    assert body[-1]["title"] == "Аврора"
    assert body[-1]["id"] == new_id


def test_post_projects_negative():
    data = {
        "title": "",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.post(base_url + '/api-v2/projects',
                         json=data, headers=headers)
    assert resp.status_code == 400


def test_put_projects_positive():
    data = {
        "title": "Рора",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.post(base_url + '/api-v2/projects',
                         json=data, headers=headers)
    body = resp.json()
    assert resp.status_code == 201
    new_id = resp.json()["id"]
    assert body["id"] == new_id
    data = {
        "title": "Ррорра",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.put(f'{base_url}/api-v2/projects/{new_id}',
                        json=data, headers=headers)
    assert resp.status_code == 200
    new_id = resp.json()["id"]
    assert body["id"] == new_id


def test_put_projects_negative():
    data = {
        "title": "Рорка",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.post(base_url + '/api-v2/projects',
                         json=data, headers=headers)
    body = resp.json()
    assert resp.status_code == 201
    new_id = resp.json()["id"]
    assert body["id"] == new_id
    data = {
        "title": "",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.put(f'{base_url}/api-v2/projects/{new_id}',
                        json=data, headers=headers)
    assert resp.status_code == 400


def test_get_projects_positive():
    data = {
        "title": "Роза",
        "users": {
            "89c7a0b6-13dc-4972-8190-a5416f674949": "admin"
        }
    }
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.post(base_url + '/api-v2/projects', json=data,
                         headers=headers)
    body = resp.json()
    assert resp.status_code == 201
    new_id = resp.json()["id"]
    assert body["id"] == new_id
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.get(f'{base_url}/api-v2/projects/{new_id}',
                        json=data, headers=headers)
    assert resp.status_code == 200
    new_id = resp.json()["id"]
    assert body["id"] == new_id


def test_get_projects_negative():
    key = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.get(base_url+'/api-v2/projects/123456789', headers=headers)
    assert resp.status_code == 404
