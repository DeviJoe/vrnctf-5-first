import os
import random

from fastapi import Request, FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from PIL import Image

app = FastAPI()
templates = Jinja2Templates(directory="templates")
static_path = Path(__file__).parent / "static"
static_dir = StaticFiles(directory=static_path)
app.mount("/static", static_dir, name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    images = []
    for image_name in os.listdir(static_path / "Task6" / "images"):
        with Image.open(static_path / "Task6" / "images" / str(image_name)) as image:
            width, height = image.size
        is_hidden = width == 800 and height == 600
        hashed_image_name = str(hash(image_name)) + ".jpg"
        os.rename(static_path / "Task6" / "images" / str(image_name),
                  static_path / "Task6" / "images" / hashed_image_name)
        images.append((hashed_image_name, is_hidden))

    random.shuffle(images)
    return templates.TemplateResponse("Task6.html", {"request": request, "images": images})
