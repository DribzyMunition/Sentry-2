from pathlib import Path
import json
from src.sentry.config import DATA_DIR, REPORTS_DIR

def build_brief() -> str:
    Path(REPORTS_DIR).mkdir(parents=True, exist_ok=True)
    infile = Path(DATA_DIR) / "filtered.jsonl"
    if not infile.exists():
        raise FileNotFoundError("Run filter first.")
    
    # Expect JSON array from AI
    try:
        data = json.loads(infile.read_text(encoding="utf-8"))
    except Exception:
        data = []
    
    lines = ["# Sentry Daily Brief\n"]
    for i, item in enumerate(data, start=1):
        lines.append(f"{i}. **{item['title']}** — {item['link']}")
    out = Path(REPORTS_DIR) / "brief.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return str(out)


