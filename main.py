from fileinput import filename
import os
from types import NoneType
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
    id = int(loadFromFile(logFile))
    with psycopg.connect(connString) as conn:
        conn.execute("SET client_encoding TO UTF8")
        with conn.cursor() as cur:
            # get last id from table select max(id) from table
            cur.execute("SELECT MAX(\"Files\".\"Id\") FROM \"Files\"")
            lastId = int(cur.fetchone()[0])
            print(lastId)
            for i in range(id, lastId + 1):              
                cur.execute("SELECT * FROM \"Files\" WHERE \"Files\".\"Id\"=%s;", (id,))
                row = cur.fetchone()
                if(row != None):
                    #debug info
                    print(row)
                    filename = row[1]
                    print(id, filename)
                    # download file
                    download(f'{url}{id}', dirPath, filename, token=authToken)
                    # save current id value into txt file
                    saveToFile("", str(id), logFile, "txt")
                id += 1