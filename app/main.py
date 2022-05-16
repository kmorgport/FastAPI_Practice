from cgi import test
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_name)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]
#origins = ["*"]
#provide a restriced list of origins that can touch your API

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    print("test")
    return {"message": "Hello World"}
    


