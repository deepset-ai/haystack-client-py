
#########################
# Raw open api client
#########################


import openapi_client as client
from pprint import pprint
from openapi_client.api import search_api
from openapi_client.model.query_request import QueryRequest

configuration = client.Configuration(
    host="http://localhost:8000"
)
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    # do requests
    request = QueryRequest(query="Who is the father of Arya Stark?")
    api_response = api_instance.query_query_post(request)
    pprint(api_response)

#################################
# Simpler Haystack client
#################################

from haystack_client import Client

client = Client(host="http://localhost:8000", deployment_type="haystack")

client.get_documents()

client.search(query="Who is the father of Arya Stark?")

# client.upload_file()

# client.delete_file()

# client.get_documents()