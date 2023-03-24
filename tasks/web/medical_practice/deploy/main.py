import os

from fastapi import Request, Form, FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from sqlalchemy import create_engine, Column, Integer, String, text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()
templates = Jinja2Templates(directory="templates")
static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")

print(db_path := os.getenv("SQLALCHEMY_DATABASE_URL"))
engine = create_engine(db_path)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
metadata = Base.metadata


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String)
    password = Column(String)
    is_admin = Column(Boolean)


metadata.drop_all(bind=engine)
metadata.create_all(bind=engine)
db = SessionLocal()
with open("static/txt/users.txt") as users_file:
    for user in users_file.readlines():
        splitted_user = user.split(" | ")
        is_admin = bool(int(splitted_user[-1]))
        db_user = Users(login=splitted_user[0], password=splitted_user[1], is_admin=is_admin)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
db.close()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("Task3.html", {"request": request, "strings": None})


@app.post("/run_query", response_class=HTMLResponse)
async def run_query(request: Request, sql: str = Form(), db: Session = Depends(get_db)):
    try:
        answer = db.execute(text("SELECT * FROM users WHERE login = " + sql))
        info = answer.fetchall()
    except:
        return templates.TemplateResponse("Task3.html", {"request": request, "info": None})

    return templates.TemplateResponse("Task3.html", {"request": request, "info": info})


@app.post('/submit_form')
async def submit_form(login: str = Form(), password: str = Form()):
    if login == "John" and password == "Cena":
        return {"message": "vrnctf{5ql_b3_0r_b3?}"}
    else:
        return {"message": "Не верный логин/пароль"}
