from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./db.db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# class Users(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     login = Column(String)
#     password = Column(String)
#
#
# class Goose(Base):
#     __tablename__ = "geese"
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     geese_string = Column(String)
#
#
# class Amogus(Base):
#     __tablename__ = "amoguses"
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     amoguses_string = Column(String)
#
#
# class Anime(Base):
#     __tablename__ = "animes"
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     animes_string = Column(String)
#
#
# class Meme(Base):
#     __tablename__ = "memes"
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     memes_string = Column(String)
#
#
# Base.metadata.create_all(bind=engine)
#
# if __name__ == '__main__':
#     db = SessionLocal()

    # with open("txt/flag.txt", "r") as memes_txt:
    #     memes = memes_txt.readlines()
    #     for meme in memes:
    #         mem = Meme(memes_string=meme)
    #         db.add(mem)
    #         db.commit()
    #         db.refresh(mem)
    #
    # with open("txt/amoguses.txt", "r") as amoguses_txt:
    #     amoguses = amoguses_txt.readlines()
    #     for amogus_line in amoguses:
    #         sus = Amogus(amoguses_string=amogus_line)
    #         db.add(sus)
    #         db.commit()
    #         db.refresh(sus)
    #
    # with open("txt/animes.txt", "r") as animes_txt:
    #     animes = animes_txt.readlines()
    #     for anime_line in animes:
    #         anim = Anime(animes_string=anime_line)
    #         db.add(anim)
    #         db.commit()
    #         db.refresh(anim)
    #
    # with open("txt/geese.txt", "r") as geese_txt:
    #     geese = geese_txt.readlines()
    #     for goose in geese:
    #         gos = Goose(geese_string=goose)
    #         db.add(gos)
    #         db.commit()
    #         db.refresh(gos)
