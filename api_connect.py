import requests


def jwt_login(url, username, password):
    token_url = url + '/users/api/token/'
    credentials = {
        'username': username,
        'password': password
    }
    response = requests.post(token_url, json=credentials)
    return response.json()['access'] if response.status_code == 200 else None


def retrieve_appointments(url, access_token):
    appointments_url = url + '/schedule/api/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(appointments_url, headers=headers)
    return response.json() if response.status_code == 200 else None
