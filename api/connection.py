import os
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR.parent / ".env"

load_dotenv(env_path)

conn = psycopg2.connect(os.getenv("DATABASE_URL"))