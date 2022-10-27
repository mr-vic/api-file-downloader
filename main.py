from fileinput import filename
import os
from dotenv import load_dotenv
from tools import download, saveToFile, loadFromFile
import psycopg

load_dotenv()
url = os.environ["url"]
dirPath = os.environ["dirPath"]
authToken= os.environ["authToken"]
connString = os.environ["connString"]
logFile = "log.txt"

if __name__ == '__main__':
    id = loadFromFile(logFile)
    with psycopg.connect(connString) as conn:
        conn.execute("SET client_encoding TO UTF8")
        with conn.cursor() as cur:
            # get last id from table select max(id) from table
            cur.execute("SELECT MAX(\"Files\".\"Id\") FROM \"Files\"")
            lastId = int(cur.fetchone()[0])
            print(lastId)
            for i in range(id, lastId):              
                cur.execute("SELECT * FROM \"Files\" WHERE \"Files\".\"Id\"=%s;", (id,))
                row = cur.fetchone()
                filename = row[1]
                print(filename)
                # download file
                download(f'{url}{getName}={getParam}', dirPath, "response.jpg", token=authToken)
                saveToFile("", str(id), logFile, "txt")