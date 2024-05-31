from pathlib import Path

BASE_DIR = Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR.joinpath('db.sqlite3'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False