import json
import requests # http requests


BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    # print(r.text)
    # print(r.headers['content-type'])
    # print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print("Probably not a good sign?")
    data = r.json()
    # print(json.dumps(data))
    for obj in data:
        # print(obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            # print("*****", r2.json())
    return data


# print(get_list())


def create_update():
    new_data = {
        "user": 1,
        "content": "Some more new Content"
    }
    # r = requests.post(BASE_URL + ENDPOINT + "1/", data=new_data)
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    print(r.text)
    # print(r.headers)
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()
    return r.text


# create_update()


def do_obj_update():
    new_data = {
        # "user": 1,
        "content": "New obj data"
    }

    # new_data = {
    #     "id": 1,
    #     "content": "Some more new Content"
    # }
    # r = requests.put(BASE_URL + ENDPOINT,  data=new_data)

    r = requests.put(BASE_URL + ENDPOINT + "1/", data=json.dumps(new_data))
    # r = requests.put(BASE_URL + ENDPOINT + "1/", data=new_data)

    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(do_obj_update())


def do_obj_delete():
    new_data = {
        "content": "New obj data"
    }
    r = requests.delete(BASE_URL + ENDPOINT + "7/")
    # new_data = {
    #     'id': 1
    #     "content": "Another more cool content"
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text



print(do_obj_delete())