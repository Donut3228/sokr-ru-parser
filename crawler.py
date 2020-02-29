import requests
import re
import os
from multiprocessing import Pool


def fetch(i):

    try:
        r = requests.get("http://www.sokr.ru/random/")
    except requests.RequestException:
        return

    # ищем уникальный айдишник страницы и добавляем в data файл с таким именем
    text = r.text
    pos = text.find('href="/card/')
    part = text[pos + 10 : pos + 35]
    uid = part.split("/")[1]
    print(i)
    filename = f"data/{uid}"
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(text)


def try_to_parse(tries_per_proc=10 ** 7, processes=64):
    p = Pool(processes)
    p.map(fetch, range(tries_per_proc))


if __name__ == "__main__":
    try_to_parse()
