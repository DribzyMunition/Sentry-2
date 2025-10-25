import feedparser
from pathlib import Path
from datetime import datetime, timezone
import json
from src.sentry.config import RSS_FEEDS, DATA_DIR
from src.sentry.models import NewsItem

def ingest_rss() -> str:
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
    out = Path(DATA_DIR) / "raw.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for url in RSS_FEEDS:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                item = NewsItem(
                    title=entry.get("title", ""),
                    link=entry.get("link", ""),
                    published=_parse(entry.get("published")),
                    summary=entry.get("summary", "")
                )
                f.write(item.model_dump_json() + "\n")
    return str(out)

def _parse(s):
    try:
        return datetime(*feedparser._parse_date(s)[:6], tzinfo=timezone.utc)
    except Exception:
        return None

