import json
from pathlib import Path
from openai import OpenAI
from src.sentry.config import OPENAI_API_KEY, DATA_DIR

def filter_with_ai() -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)
    infile = Path(DATA_DIR) / "raw.jsonl"
    outfile = Path(DATA_DIR) / "filtered.jsonl"

    if not infile.exists():
        raise FileNotFoundError("Run ingest first.")

    items = [json.loads(line) for line in infile.open("r", encoding="utf-8")]

    # Build prompt
    text = "\n".join([f"- {i['title']} ({i['link']})" for i in items])
    prompt = f"""
You are a news analyst. Rank the following headlines by global and financial importance.
Skip trivial news. Return JSON list with objects: title, link, rank (1=highest).
Headlines:
{text}
"""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = resp.choices[0].message.content
    # Save raw output
    outfile.write_text(content, encoding="utf-8")
    return str(outfile)

