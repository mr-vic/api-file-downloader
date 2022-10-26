from fileinput import filename
import requests
import os
from dotenv import load_dotenv
#import download

load_dotenv()
getName = os.environ["getName"]
getParam = os.environ["getParam"]
url = os.environ["url"]
authToken= os.environ["authToken"]

def saveToFile(dirPath, content, fileName):
    with open(fileName, "wb") as f:
        f.write(content)

def download(endpoint, dirPath, fileName, token = None):
    headers = {"Authorization": f'Bearer {token}'}
    res = requests.get(endpoint, headers=headers)
    contentType = res.headers['content-type']
    saveToFile(dirPath, res.content, fileName)
    return res

if __name__ == '__main__':
    print(download(f'{url}{getName}={getParam}', "C:\\backup", "response.jpg", token=authToken))