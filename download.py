from asyncio.windows_events import NULL
from contextlib import nullcontext
import requests

def download(endpoint, data, dirPath, token = None):
    headers = {"Authorization": "Bearer {token}"}
    header = requests.get(endpoint, data=data, headers=headers)
    return header
