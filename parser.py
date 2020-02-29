import re
import os


dirs = os.listdir('data')

def main():

    words = []

    # Вытаскиваем сокращения из скачанного html документа
    for filename in dirs:
        with open(f"data/{filename}") as f:
            tokens = re.findall(r'<h1 itemprop="term".*>(.*)</h1>', f.read())
            words.extend(tokens)

    res = []

    # Убираем все лишние символы
    for word in words:
        chars = ['.', '-', '!', '*', '(', ')', '/', '"', '?', '⋅', '«', '»']
        for ch in chars:
            if ch in word:
                word = word.replace(ch, '')
        res.append(word)

    # Разделяем слова, которые состоят из нескольких слов
    fin_res = []
    for r in res:
        tokens = r.split(' ')
        tokens = [x.lower() for x in tokens]
        fin_res.extend(tokens)

    # Записываем в txt отсортированный сет, от всех слов
    with open('res.txt', 'w') as f:
        f.write('\n'.join(sorted(set(fin_res))))

def parse():
    main()

if __name__ == "__main__":
    main()