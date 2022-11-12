from urllib import request
import urllib

urls = []
size = 0
i = 0
while size < 100:
    url = f"https://habr.com/ru/post/{698000 + i}/"
    print(i, size)
    try:
        with request.urlopen(url) as response:
            text = response.read()
    except urllib.error.HTTPError:
        i += 1
    else:
        urls.append(url)
        size += 1
        i += 1

with open("urls.txt", "w", encoding="utf-8") as fout:
    for url in urls:
        print(url, file=fout)
