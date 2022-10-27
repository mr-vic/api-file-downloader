import requests

def saveToFile(dirPath, content, fileName):
    print(dirPath + fileName)
    with open(dirPath + fileName, "wb") as f:
        f.write(content)

def download(endpoint, dirPath, fileName, token = None):
    headers = {"Authorization": f'Bearer {token}'}
    res = requests.get(endpoint, headers=headers)
    contentType = res.headers['content-type']
    saveToFile(dirPath, res.content, fileName)
    return res
