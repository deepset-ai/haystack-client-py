import openapi_client
from openapi_client.api import search_api, file_upload_api, document_api
from openapi_client.models import QueryRequest, FilterRequest

from typing import Dict
import requests

#TODO:
#class BaseClient:


class HaystackClient:
    def __init__(self, host="http://localhost:8000"):
        self.configuration = openapi_client.Configuration(
            host=host
        )
        self.client = openapi_client.ApiClient(self.configuration)

    def search(self, query: str, params: Dict = None):
        # Create an instance of the API class
        api_instance = search_api.SearchApi(self.client)

        # Send request
        request = QueryRequest(query=query, params=params)
        api_response = api_instance.query(request)

        return api_response

    def get_documents(self, filters: Dict = None):
        # Create an instance of the API class
        api_instance = document_api.DocumentApi(self.client)

        # Send request
        request = FilterRequest(filters={})
        api_response = api_instance.get_documents(request)

        return api_response


    # def upload_file(self, file_path, meta):
    #     api_instance = file_upload_api.FileUploadApi(self.client)
    #     request = FileUploadRequest()
    #     api_response = api_instance.file_upload_file_upload_post(request)



class HaystackHubClient:

    def __init__(self, user, password):
        self.token = self.authenticate(user, password)


    def authenticate(self, user, password):

        url = "https://api.haystack-hub.com/api/v1/auth/token"

        payload = f'{{"email": "{user}","password": "{password}","expire_in": 36000}}'
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()["access_token"]


    def search(self, query: str, params: Dict = None, workspace="default"):

        url = f"http://api.haystack-hub.com/api/v1/workspaces/{workspace}/search"

        payload = f'{{"queries": ["{query}"]}}'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response
