#  Copyright (c) 2023 AMProduction

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return "Welcome to the books API"
