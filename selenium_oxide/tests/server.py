import uvicorn
import os
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


def main():
    app = FastAPI()

    app.mount("/static", StaticFiles(directory="static"), name="static")

    templates = Jinja2Templates(directory="templates")

    @app.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        return templates.TemplateResponse(request=request, name="home.html")

    @app.get("/login", response_class=HTMLResponse)
    async def login_page(request: Request):
        return templates.TemplateResponse(request=request, name="login.html")

    @app.post("/login", response_class=HTMLResponse)
    async def login(
        request: Request,
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
    ):
        return templates.TemplateResponse(
            request=request, name="login.html", context={"username": username}
        )

    uvicorn.run(app, host="0.0.0.0", port=1337, log_level="warning")


# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": id}
#     )

if __name__ == "__main__":
    cwd = Path(os.getcwd())
    new_root = cwd / "selenium_oxide" / "tests"
    os.chdir(new_root)
    main()
