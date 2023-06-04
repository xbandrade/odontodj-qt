import requests
from PyQt5.QtCore import QThread, pyqtSignal


class VerificationThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, credentials, url):
        super().__init__()
        self.credentials = credentials
        self.url = url

    def run(self):
        token_url = self.url + '/users/api/token/'
        response = requests.post(token_url, json=self.credentials)
        access_token = response.json().get('access', '') if response.ok else ''
        self.finished.emit(access_token)


def retrieve_appointments(url, access_token):
    api_url = url + '/schedule/api/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(api_url, headers=headers)
    return response.json().get('results') if response.ok else None


def retrieve_datetimes(url, access_token):
    api_url = url + '/schedule/api/datetime/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(api_url, headers=headers)
    return response.json().get('available_datetimes') if response.ok else None


def retrieve_procedures(url, access_token):
    api_url = url + '/schedule/api/procedure/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(api_url, headers=headers)
    return response.json().get('results') if response.ok else None


def schedule_appointment(url, access_token, procedure, date, time, user=None):
    api_url = url + '/schedule/api/'
    request_json = {
        'procedure': procedure,
        'date': date,
        'time': time
    }
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    try:
        response = requests.post(
            api_url,
            data=request_json,
            headers=headers
        )
        return response.ok
    except requests.exceptions.RequestException:
        return False


def add_new_patient(url, access_token, data):
    api_url = url + '/users/api/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    try:
        response = requests.post(
            api_url,
            data=data,
            headers=headers
        )
        if not response.ok:
            print(response.json())
        return response.ok
    except requests.exceptions.RequestException:
        return False


def retrieve_patient_details(url, access_token, patient_id):
    api_url = url + '/users/api/' + patient_id + '/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(api_url, headers=headers)
    return response.json() if response.ok else None


def update_patient(url, access_token, data, patient_id):
    api_url = url + '/users/api/' + patient_id + '/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    try:
        response = requests.patch(
            api_url,
            data=data,
            headers=headers
        )
        if not response.ok:
            print(response.json())
        return response.ok
    except requests.exceptions.RequestException:
        return False


def retrieve_procedure_details(url, access_token, procedure_id):
    api_url = url + '/schedule/api/procedure/' + procedure_id + '/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(api_url, headers=headers)
    return response.json() if response.ok else None


def update_procedure(url, access_token, data, procedure_id):
    api_url = url + '/schedule/api/procedure/' + procedure_id + '/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    try:
        response = requests.patch(
            api_url,
            data=data,
            headers=headers
        )
        if not response.ok:
            print(response.json())
        return response.ok
    except requests.exceptions.RequestException:
        return False
