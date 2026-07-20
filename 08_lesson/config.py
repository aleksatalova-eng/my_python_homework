import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ru.yougile.com"
TOKEN = os.getenv("TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
