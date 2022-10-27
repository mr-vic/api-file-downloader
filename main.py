from fileinput import filename
#import requests
import os
from dotenv import load_dotenv
from download import download

load_dotenv()
getName = os.environ["getName"]
getParam = os.environ["getParam"]
url = os.environ["url"]
dirPath = os.environ["dirPath"]
authToken= os.environ["authToken"]

if __name__ == '__main__':
    
    print(download(f'{url}{getName}={getParam}', dirPath, "response.jpg", token=authToken))