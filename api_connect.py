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
    appointments_url = url + '/schedule/api/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(appointments_url, headers=headers)
    return response.json().get('results') if response.ok else None


def retrieve_datetimes(url, access_token):
    appointments_url = url + '/schedule/api/datetime/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(appointments_url, headers=headers)
    return response.json().get('available_datetimes') if response.ok else None


def retrieve_procedures(url, access_token):
    appointments_url = url + '/schedule/api/procedure/'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(appointments_url, headers=headers)
    return response.json().get('results') if response.ok else None
