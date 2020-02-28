import requests
import re
import os
from multiprocessing import Pool

def fetch(i):

    try:
        r = requests.get('http://www.sokr.ru/random/')
    except requests.RequestException:
        return

    # ищем уникальный айдишник страницы и добавляем в data файл с таким именем
    text = r.text
    pos = text.find('href="/card/')
    part = text[pos+10:pos+35]
    uid = part.split('/')[1]
    print(i)
    filename = f'data/{uid}'
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(text)


if __name__ == "__main__":
    p = Pool(64)
    p.map(fetch, range(10**7))