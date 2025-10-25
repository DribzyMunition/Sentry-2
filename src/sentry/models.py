from pydantic import BaseModel, HttpUrl
from datetime import datetime

class NewsItem(BaseModel):
    title: str
    link: HttpUrl
    published: datetime | None = None
    summary: str = ""

