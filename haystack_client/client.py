import openapi_client
from openapi_client.api import search_api, file_upload_api, document_api
from openapi_client.models import QueryRequest, FilterRequest

from typing import Dict


class Client:
    def __init__(self, host="http://localhost:8000", deployment_type="haystack"):
        if deployment_type == "haystack":
            self.configuration = openapi_client.Configuration(
                host=host
            )
            self.client = openapi_client.ApiClient(self.configuration)
        else:
            raise NotImplementedError

    def search(self, query: str, params: Dict = None):
        # Create an instance of the API class
        api_instance = search_api.SearchApi(self.client)

        # Send request
        request = QueryRequest(query=query, params=params)
        api_response = api_instance.query_query_post(request)

        return api_response

    def get_documents(self, filters: Dict = None):
        # Create an instance of the API class
        api_instance = document_api.DocumentApi(self.client)

        # Send request
        request = FilterRequest(filters={})
        api_response = api_instance.get_documents_by_filter_documents_get_by_filters_post(request)

        return api_response


    # def upload_file(self, file_path, meta):
    #     api_instance = file_upload_api.FileUploadApi(self.client)
    #     request = FileUploadRequest()
    #     api_response = api_instance.file_upload_file_upload_post(request)



