from fastapi import Request, Form, FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="templates")
static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("Task1.html", {"request": request})


@app.post('/submit_form')
async def submit_form(login: str = Form(), password: str = Form(), secret_key: str = Form()):
    if login == "pizza" and password == "pepperoni" and secret_key == "doublePepperoni":
        return {"message": "vrnctf{1_l0v3_7h47_p3pp3r0n1}"}
    else:
        return {"message": "Не верный логин/пароль/ключ"}
