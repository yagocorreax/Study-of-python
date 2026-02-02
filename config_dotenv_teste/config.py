import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "database": os.getenv('DATABASE'),
    "port": os.getenv('PORT'),
    "password": os.getenv('PASSWORD'),
    "user": os.getenv('USERNAMEE')
}