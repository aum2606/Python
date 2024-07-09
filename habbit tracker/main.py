import requests
from datetime import datetime
PIXELA = "https://pixe.la/v1/users"
USERNAME = "aumparmar"
TOKEN = "XXXXXXXX"
GRAPH_ID ="graph2"
today = datetime.now()
HEADER = {
    "X-USER-TOKEN": TOKEN
}


#creating the user
params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(PIXELA,json=params)
# print(response.text)


# creating Graph
GRAPH_ENDPOINT = f"{PIXELA}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "int",
    "color": "ajisai"
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=HEADER)
# print(response.text)

POST_ENDPOINT = f"{PIXELA}/{USERNAME}/graphs/{GRAPH_ID}"
post_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today")
}
# response = requests.post(url=POST_ENDPOINT,json=post_param, headers=HEADER)
# print(response.text)

#PUT
PUT_ENDPOINT = f"{PIXELA}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
put_params={
    "quantity": "8"
}
# response = requests.put(url=PUT_ENDPOINT,json=put_params, headers=HEADER)
# print(response.text)

#DELETE
DELETE_ENDPOINT = f"{PIXELA}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=DELETE_ENDPOINT, headers=HEADER)
# print(response.text)