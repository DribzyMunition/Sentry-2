import typer
from src.sentry.ingest.rss import ingest_rss
from src.sentry.filter.ai import filter_with_ai
from src.sentry.report.brief import build_brief

app = typer.Typer(no_args_is_help=True)

@app.command()
def ingest():
    path = ingest_rss()
    print(f"Ingested → {path}")

@app.command()
def filter():
    path = filter_with_ai()
    print(f"AI filtered → {path}")

@app.command()
def brief():
    path = build_brief()
    print(f"Brief ready → {path}")

if __name__ == "__main__":
    app()

