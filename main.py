from fileinput import filename
import os
from dotenv import load_dotenv
from tools import download
import psycopg

load_dotenv()
getName = os.environ["getName"]
getParam = os.environ["getParam"]
url = os.environ["url"]
dirPath = os.environ["dirPath"]
authToken= os.environ["authToken"]
connString = os.environ["connString"]


if __name__ == '__main__':

    with psycopg.connect(connString) as conn:
        conn.execute("SET client_encoding TO UTF8")
        with conn.cursor() as cur:
            id = 2
            cur.execute("SELECT * FROM \"Files\" WHERE \"Files\".\"Id\"=%s;", (id,))
            row = cur.fetchone()
            filename = row[1]
            print(filename)


    
    #print(download(f'{url}{getName}={getParam}', dirPath, "response.jpg", token=authToken))