import requests

def saveToFile(dirPath, content, fileName, type="bin"):
    if type == "bin":
        with open(dirPath + fileName, "wb") as f:
            f.write(content)
    elif type == "txt":
        with open(dirPath + fileName, "w") as f:
            f.write(content)

def download(endpoint, dirPath, fileName, token = None):
    headers = {"Authorization": f'Bearer {token}'}
    res = requests.get(endpoint, headers=headers)
    contentType = res.headers['content-type']
    saveToFile(dirPath, res.content, fileName, "bin")
    return res

def loadFromFile(fileName):
    result = ""
    with open(fileName) as f:
        result = f.readline()
    return result
