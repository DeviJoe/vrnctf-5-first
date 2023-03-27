# Library issues - Решение

Сайт предоставляем нам директории и файлы в них

Да, их много, а файлов и того больше, и кто знает(<s>кроме меня</s>), где там флаг.

Есть два пути решения:
 - Копать лопатой
 - Воспользоваться экскаватором
<br>

# Путь лопаты:
Перебирать все папки и файлы пока не найдешь

Время решения: 30мин-1час

# Путь экскаватора
Пишем скрипт(ура, кодинг!)

Вот пример скрипта, перебирающего директории
```Python
import requests
from bs4 import BeautifulSoup


def dfs(url, visited):
    visited.add(url)
    print(url)

    # Скачиваем HTML-код страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if "vrnctf" in soup.get_text():
        print(soup.get_text())
        exit()
    # Находим все ссылки на странице
    links = soup.find_all('a')

    # Рекурсивно обходим все найденные ссылки
    for link in links:
        href = link.get('href')
        if href.startswith('http') and href not in visited:
            dfs(href, visited)


url = "http://127.0.0.1:8000/"
visited = set()

dfs(url, visited)
```

Пишется быстро и просто

Время решения: 15 минут писать код, 1-2 минуты поиск флага

Флаг - <b>vrnctf{7h3_b166357_l1br4ry_1_3v3r_533n}