import os
from time import sleep
# os.system("venv/bin/python3 \"Rising force\" &")

import subprocess
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
while True:
    keys = set([row.decode() for row in r.keys('*')])
    # os.system("cd crawler")
    # os.system("pwd")
    for i in keys:
        os.system("""cd crawler; scrapy crawl photo_crawler -a email=trynext@yandex.ru -a password=qwertyuiop[] -a target_username=""" + r.get(i).decode() + """; cd ..; venv/bin/python3 file_to_db.py """ + r.get(i).decode()+" &")
    try:
        print('\n\n', *keys)
        r.delete(*keys)
    except:
        pass
    sleep(15)
    # anatolijsharij
