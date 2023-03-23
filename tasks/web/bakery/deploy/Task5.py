from pathlib import Path

from fastapi import FastAPI, Response
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")


@app.get("/")
async def flag(request: Request, response: Response):
    cookies = request.cookies
    response = templates.TemplateResponse("Task5.html", {"response": response, "request": request})

    if "logged_in" not in cookies.keys():
        response.set_cookie(key="logged_in", value="False", httponly=True)
    elif cookies["logged_in"] == "True":
        return {"Flag": "vrnctf{5000_d3l1c10u5_4nd_u53ful}"}

    return response
