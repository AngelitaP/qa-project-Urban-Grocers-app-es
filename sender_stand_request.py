import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body):
    response=post_new_user(data.user_body)
    auth_token=response.json()["authToken"]
    variable_headers=data.headers.copy()
    variable_headers["Authorization"]=f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  headers= variable_headers, json=kit_body)