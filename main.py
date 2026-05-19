from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from core.database import engine

app = FastAPI()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
