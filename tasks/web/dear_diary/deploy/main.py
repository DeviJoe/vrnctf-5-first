import os

from fastapi import FastAPI, Depends, Form
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, Boolean
from starlette import status
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from pathlib import Path

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


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    text = Column(String)
    visible = Column(Boolean)


def fill_tables():
    db = SessionLocal()

    with open("static/txt/posts.txt", "r") as posts_txt:
        posts = posts_txt.readlines()
        for post in posts:
            splitted_post = post.split(" | ")
            visible = False if int(splitted_post[-1]) == 0 else True
            post_db = Post(title=splitted_post[0], text=splitted_post[1], visible=visible)
            db.add(post_db)
            db.commit()
            db.refresh(post_db)

    db.close()


metadata.drop_all(bind=engine)
metadata.create_all(bind=engine)
fill_tables()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, db: Session = Depends(get_db)):
    posts = db.query(Post).all()

    return templates.TemplateResponse("Task4.1.html", {"request": request, "posts": posts})


@app.get('/posts/{post_number}')
async def get_post_page(post_number: int, request: Request, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_number).first()

    return templates.TemplateResponse("Task4.2.html", {"request": request, "post": post, "update": False, "new": False})


@app.get('/update_post/{post_number}')
async def update_post_page(post_number: int, request: Request, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_number).first()

    return templates.TemplateResponse("Task4.2.html", {"request": request, "post": post, "update": True, "new": False})


@app.post('post_post/{post_number}')
async def post_post_page(post_number: int,
                         new_title: str,
                         new_text: str,
                         db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_number).first()
    post.title = new_title
    post.text = new_text
    db.commit()

    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)


@app.get('/new_post')
async def new_post_page(request: Request, db: Session = Depends(get_db)):
    post = Post()
    db.add(post)
    db.commit()
    db.refresh(post)

    return templates.TemplateResponse("Task4.2.html", {"request": request, "post": post, "update": True, "new": True})


@app.post('/new_post/{post_number}')
async def create_new_post_page(post_number: int,
                               title: str = Form(),
                               text: str = Form(),
                               db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_number).first()
    post.title = title
    post.text = text
    post.visible = True
    db.commit()
    db.refresh(post)

    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)
