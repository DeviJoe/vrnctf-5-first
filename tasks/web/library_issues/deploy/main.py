import os
import random
import shutil
import string

from fastapi import Request, FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

file_dict = dict()


def generate_random_dirs(root_path, depth, max_dirs, max_files):
    """
    Функция генерирует случайную иерархию директорий с рандомными названиями
    и записывает в случайную директорию текстовый файл.

    :param root_path: str, путь к корневой директории
    :param depth: int, глубина иерархии директорий
    :param max_dirs: int, максимальное количество директорий в каждой папке
    :param max_files: int, максимальное количество файлов в каждой папке
    """
    # очищаем папку перед генерацией
    if os.path.exists(root_path):
        shutil.rmtree(root_path)

    # генерируем случайное название директории
    def random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    # генерируем случайную иерархию директорий
    def make_random_dirs(root_path, depth, max_dirs, max_files):
        if depth == 0:
            return
        num_dirs = random.randint(1, max_dirs)
        for i in range(num_dirs):
            dir_name = random_string(10)
            dir_path = os.path.join(root_path, dir_name)
            os.mkdir(dir_path)
            num_files = random.randint(1, max_files)
            for j in range(num_files):
                file_name = random_string(10) + ".txt"
                file_path = os.path.join(dir_path, file_name)
                file_dict[file_name] = file_path
                with open(file_path, "w") as f:
                    f.write("This is a test file.")

            make_random_dirs(dir_path, depth - 1, max_dirs, max_files)

    # генерируем иерархию директорий
    os.mkdir(root_path)
    make_random_dirs(root_path, depth, max_dirs, max_files)

    # записываем текстовый файл в случайную папку
    all_dirs = []
    for root, dirs, files in os.walk(root_path):
        for dir in dirs:
            all_dirs.append(os.path.join(root, dir))

    random_dir = random.choice(all_dirs)
    file_name = random_string(10) + ".txt"
    file_path = os.path.join(random_dir, file_name)
    file_dict[file_name] = file_path
    print(file_path)
    with open(file_path, "w") as f:
        f.write(flag)


app = FastAPI()
templates = Jinja2Templates(directory="templates")
static_path = Path(__file__).parent / "static"
static_dir = StaticFiles(directory=static_path)
app.mount("/static", static_dir, name="static")

flag = "vrnctf{7h3_b166357_l1br4ry_1_3v3r_533n}"
generate_random_dirs(static_path / "root", 5, 10, 10)


@app.get('/directory/{path:path}')
def list_directory(path, request: Request):
    full_path = os.path.join(static_path / "root", path)
    dirs = []
    files = []
    for item in os.listdir(full_path):
        item_path = os.path.join(full_path, item)
        if os.path.isdir(item_path):
            dirs.append({
                'name': item,
                'path': os.path.join(path, item),
                'dirs': [],
                'files': []
            })
        else:
            files.append(item)

    return templates.TemplateResponse("Task7.2.html", {
        "request": request, "path": path, "dirs": dirs, "files": files, "first": False
    })


@app.get("/")
async def directory(request: Request):
    # получение списка файлов и директорий в текущей директории
    dir_path = static_path / "root/"
    items = os.listdir(dir_path)
    dirs = [item for item in items if os.path.isdir(os.path.join(dir_path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(dir_path, item))]

    return templates.TemplateResponse("Task7.2.html", {
        "request": request, "dirs": dirs, "files": files, "first": True
    })


@app.get("/file/{filename}")
async def open_file(request: Request, filename):
    file_path = file_dict[filename]
    with open(file_path, 'r') as file:
        text = file.readline()

    return templates.TemplateResponse("Task7.1.html", {"request": request, "text": text})
