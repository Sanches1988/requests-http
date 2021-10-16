import json
import os
import requests
from requests.models import Response

TOKEN = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url =  "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url=url, headers=headers, params=params)
        return response.json()
        

    def upload_file(self, file_path, file_name):
        href = self.upload(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(file_name, "rb"))
        response.raise_for_status
        if response.status_code == 201:
            print("Успех")


if __name__ == '__main__':
    token = TOKEN
    uploader = YaUploader(token)
    uploader.upload_file("Netology/Test.txt", "Test.txt")


