#  Copyright (c) 2023 AMProduction

from fastapi import FastAPI, HTTPException

from . import database
from . import schemas

app = FastAPI()


@app.get("/")
def get_root():
    return "Welcome to the books API"


@app.get("/book/{book_id}")
def retrieve_book(book_id: int):
    try:
        return database.get_book(book_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=repr(e))


@app.post("/book/")
def create_book(request: schemas.BookAuthorPayload):
    database.add_book(convert_into_book_db_model(request.book), convert_into_author_db_model(request.author))
    return f"New book added {request.book.title} {request.book.number_of_pages}. New author added " \
           f"{request.author.first_name} {request.author.last_name}"


def convert_into_book_db_model(book: schemas.Book):
    return database.Book(title=book.title, number_of_pages=book.number_of_pages)


def convert_into_author_db_model(author: schemas.Author):
    return database.Author(first_name=author.first_name, last_name=author.last_name)
