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
    return templates.TemplateResponse("Task3.html", {"request": request})


@app.post('/submit_form')
async def submit_form(login: str = Form(), password: str = Form()):
    if login == "or 1=1--" in login or "or 1=1" in login:
        return {"message": "vrnctf{5ql_b3_0r_b3?}"}
    else:
        return {"message": "Login/Password is not correct!"}
