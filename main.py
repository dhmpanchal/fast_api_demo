from fastapi import FastAPI, Depends
from blog.routes.blog_routs import blog_router

app = FastAPI()
app.include_router(blog_router)