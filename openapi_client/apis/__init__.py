
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.document_api import DocumentApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.document_api import DocumentApi
from openapi_client.api.feedback_api import FeedbackApi
from openapi_client.api.file_upload_api import FileUploadApi
from openapi_client.api.search_api import SearchApi
