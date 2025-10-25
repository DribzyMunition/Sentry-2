import os
from dotenv import load_dotenv

load_dotenv()

RSS_FEEDS = [u.strip() for u in os.getenv("SENTRY_RSS_FEEDS", "").split(",") if u.strip()]
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATA_DIR = "data"
REPORTS_DIR = "reports"

