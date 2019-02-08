import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
image_path = os.path.join(os.getcwd(), "logo.png")

headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTQ5NjI2NDIyLCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwib3JpZ19pYXQiOjE1NDk2MjYxMjJ9.mNjLyhfUiNkpedKUOf2DZsY0Xag7rI6xanFGzcDa4XY'
}


data = {
    'username': "bdg4",
    'email': "bdg4@example.com",
    'password': "pass#123",
    'password2': "pass#123"
}

# data = {
#     'username': "admin",
#     'password': "pass#123",
# }
r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()#['token']
print(r.text)


# REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'

# r = requests.post(url=REFRESH_ENDPOINT, data=json.dumps({'token': token}), headers=headers)
# token = r.json()
# print(token)



# get_endpoint = ENDPOINT + str(14)
# r = requests.get(get_endpoint)
# print(r.status_code)

# headers = {"Authorization": "JWT " + token}

# post_data = {"content": "Updated random contents"}
# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     posted_response = requests.post(ENDPOINT, data=post_data, files=file_data, headers=headers)
#     # posted_response = requests.put(ENDPOINT +"25/", data=post_data, files=file_data, headers=headers)
#     print(posted_response.text)
#     # get_endpoint = ENDPOINT + str(12)







#
# import requests
# import json
# import os
#
# ENDPOINT = "http://127.0.0.1:8000/api/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'
# data = {'username': "admin", 'password': "pass#123"}
# headers = {"content-type": "application/json"}
#
#
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data),  headers=headers)
# token = r.json()['token']
# print(token)
#
#
#
#
# # refresh = requests.post(url=REFRESH_ENDPOINT, data=json.dumps({'token': token}), headers=headers)
# # refresh_token = refresh.json()
# # print(refresh_token)
#
# image_path = os.path.join(os.getcwd(), "logo.png")
#
# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }
#
#
# with open(image_path, 'rb') as image:
#     file_data = {
#         "image": image
#     }
#
#
# # post_data = json.dumps({"content": "Another new post by admin"})
# data = {"content": "Another new post by admin"}
# # json_data = json.dumps({"content": "Another new post by admin"})
#
# # posted_response = requests.post(ENDPOINT, data=data, headers=headers, files=file_data) # post image
# posted_response = requests.put(ENDPOINT + str(16) + "/", data=data, headers=headers, files=file_data)# updating image
#
# print(posted_response.text)
#
#
# with open(image_path, 'rb') as image:
#     file_data = {
#         "image": image
#     }
#
# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }
#
#
# # jsn_data = json.dumps({"content": "Update"})
# data = {"content": "Update"}
# posted_response = requests.put(ENDPOINT + str(16) + "/", data=data, headers=headers) # updating content
# print(posted_response.text)






# get_endpoint = ENDPOINT + str(1)




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
