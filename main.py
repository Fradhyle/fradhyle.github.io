from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from workers import asgi
from workers import WorkerEntrypoint
from workers import Response

app = FastAPI()


# @app.get("/style.css")
# def get_css():
#     css_content = Path("style.css").read_text(encoding="utf-8")
#     return Response(content=css_content, media_type="text/css")


@app.get("/", response_class=HTMLResponse)
class Default(WorkerEntrypoint):
    async def fetch(self, request, lang: str = "ko"):
        if lang == "en":
            html_content = Path("index_en.html").read_text("utf-8")
            return HTMLResponse(content=html_content)
        else:
            html_content = Path("index.html").read_text("utf-8")
            return HTMLResponse(content=html_content)
