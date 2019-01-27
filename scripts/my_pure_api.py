import json
import requests  # http requests

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list(id=None):
    # data = json.dumps({"id": "5"})
    data = json.dumps({})
    if id is not None:
        data = json.dumps({"id": id})
    r = requests.get(BASE_URL + ENDPOINT, data=data)
    # print(r.text)
    # print(r.headers['content-type'])
    # print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print("Probably not a good sign?")
    data = r.json()
    return data


# print(get_list())


def create_update():
    new_data = {
        "user": 1,
        "content": "Rocking new Content"
    }
    data = json.dumps(new_data)
    print(type(data))
    r = requests.post(BASE_URL + ENDPOINT, data=data)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


# print(create_update())


def do_obj_update():
    new_data = {
        "id": "8",
        "content": "Some New obj data"
    }
    # r = requests.put(BASE_URL + ENDPOINT + "1/", data=json.dumps(new_data))
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()
    return r.json()


# print(do_obj_update())


def do_obj_delete():
    new_data = {
        "id": "8",
        "content": "New obj data"
    }
    r = requests.delete(BASE_URL + ENDPOINT, data= json.dumps(new_data))
    # new_data = {
    #     'id': 1
    #     "content": "Another more cool content"
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(get_list())
# print(do_obj_update())
# print(do_obj_delete())


base_url = "http://127.0.0.1:8000/"

endpoint = "api/post/"


def get_blog_list():
    data = json.dumps({"id": "1"})
    r = requests.get(base_url + endpoint, data=data)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def create_blog():
    data = {
        "author": "1",
        "title": "new title",
        "content": "Some new content"
    }
    r = requests.post(base_url + endpoint, data=json.dumps(data))
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def update_blog():
    data = {
        "id": "4",
        "author": "1",
        "content": "This content is updated"
    }

    r = requests.put(base_url+endpoint, data=json.dumps(data))
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def delete_blog():
    data = {
        "id": "4"
    }
    r = requests.delete(base_url+endpoint, data=json.dumps(data))
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

print(delete_blog())
# print(update_blog())
# print(create_blog())
# print(get_blog_list())