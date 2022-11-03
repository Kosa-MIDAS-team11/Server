import os

from dotenv import find_dotenv, load_dotenv

__config_file = find_dotenv()
load_dotenv(__config_file)


class DBConfig:
    URL = os.environ['DATABASE_URL']


class JWTConfig:
    ACCESS_TIMEOUT = os.environ['JWT_ACCESS_TIME']
    ALGORITHM = os.environ['ALGORITHM']
    SECRET = os.environ['SECRET']
