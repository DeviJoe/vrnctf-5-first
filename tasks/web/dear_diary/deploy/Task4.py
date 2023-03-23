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

SQLALCHEMY_DATABASE_URL = "sqlite:///./database/db.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


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


class Goose(Base):
    __tablename__ = "geese"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    geese_string = Column(String)


class Amogus(Base):
    __tablename__ = "amoguses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amoguses_string = Column(String)


class Anime(Base):
    __tablename__ = "animes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    animes_string = Column(String)


class Meme(Base):
    __tablename__ = "memes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    memes_string = Column(String)


class Card:
    def __init__(self, text_list: list[str], start: int, end: int):
        self.text = "\n".join(text_list)
        self.id_start = start
        self.id_end = end


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    text = Column(String)
    visible = Column(Boolean)


def fill_tables():
    db = SessionLocal()

    with open("static/txt/memes.txt", "r") as memes_txt:
        memes = memes_txt.readlines()
        for meme in memes:
            mem = Meme(memes_string=meme)
            db.add(mem)
            db.commit()
            db.refresh(mem)

    with open("static/txt/amoguses.txt", "r") as amoguses_txt:
        amoguses = amoguses_txt.readlines()
        for amogus_line in amoguses:
            sus = Amogus(amoguses_string=amogus_line)
            db.add(sus)
            db.commit()
            db.refresh(sus)

    with open("static/txt/animes.txt", "r") as animes_txt:
        animes = animes_txt.readlines()
        for anime_line in animes:
            anim = Anime(animes_string=anime_line)
            db.add(anim)
            db.commit()
            db.refresh(anim)

    with open("static/txt/geese.txt", "r") as geese_txt:
        geese = geese_txt.readlines()
        for goose in geese:
            gos = Goose(geese_string=goose)
            db.add(gos)
            db.commit()
            db.refresh(gos)

    with open("static/txt/posts.txt", "r") as posts_txt:
        posts = posts_txt.readlines()
        for post in posts:
            splitted_post = post.split(" | ")
            visible = False if int(splitted_post[-1]) == 0 else True
            post_db = Post(title=splitted_post[0], text=splitted_post[1], visible=visible)
            db.add(post_db)
            db.commit()
            db.refresh(post_db)

    with open("static/txt/users.txt", "r") as users_txt:
        users = users_txt.readlines()
        for user in users:
            splitted_user = user.split(" | ")
            user_db = Users(login=splitted_user[0], password=splitted_user[-1])
            db.add(user_db)
            db.commit()
            db.refresh(user_db)

    db.close()


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
fill_tables()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")


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
