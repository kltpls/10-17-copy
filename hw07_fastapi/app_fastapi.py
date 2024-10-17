import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from markupsafe import escape
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def landing_page(request: Request):
    return templates.TemplateResponse(request=request, name='landing.html', context={"title": 'Home'})


@app.get('/blog')
def blog_list(request: Request):
    return templates.TemplateResponse(request=request, name='blog.html', context={"title": "blog post"})


@app.get('/about')
def about_page(request: Request):
    return templates.TemplateResponse(request=request, name='about_me.html', context={"title": "about me"})


if __name__ == '__main__':
    uvicorn.run(app, port=8000) # host="0.0.0.0",
