import requests
import json
import os

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
image_path = os.path.join(os.getcwd(), "logo.png")

headers = {
    "Content-Type": "application/json"
}

data ={
    "username": "admin",
    "password": "pass#123"
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print(token)

refresh_data = {
    'token': token
}
refresh_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
refresh_token = refresh_response.json() #['token']
print(refresh_token)


# get_endpoint = ENDPOINT + str(1)
# post_data = json.dumps({"content": "Post by Bristy"})
#
# r = requests.get(get_endpoint)
# # print(r.text)
#
# r2 = requests.get(ENDPOINT)
# # print(r2.text)
#
# post_headers ={
#     "content-type": "application/json"
# }
#
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)






#
# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         print(img_path)
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do_img(method='post', data={"user": 1, "content": ""}, is_json=False, img_path=image_path)
# do_img(method='put', data={"id": 6, "user": 1, "content": "Great Content"}, is_json=False, img_path=image_path)

#
# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#



# end_point = "http://127.0.0.1:8000/api/status/7/"


# def check_statusapi_detail(method='get', data={}, is_json=False, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path:
#         with open(image_path, 'rb') as image:
#             file_data={"image": image}
#             r = requests.request(method, end_point, data=json.dumps(data), headers=headers,  files=file_data)
#     else:
#         r = requests.request(method, end_point, data=data)
#     print(r.text)
#     print(r.status_code)
#     return r




# check_statusapi_detail(method='put', data={"id": 2, "user": 1, "content": "I am Changing this content"}, is_json=False)
# check_statusapi_detail(method='delete', data={"id": 7}, is_json=False)



# do(data={'id': 10})
# do(method='delete', data={'id': 13})
# do(method='put', data={'id': 10, "content": "Some cool new content", "user": 1})
# do(method='post', data={"content": "delete content", "user": 1})
