#import tkinter

from schemas import database
from schemas.database import SessionLocal, get_db
from schemas.models import Book
from sqlalchemy.orm import Session

import tkinter as tk
from app import App

database.Base.metadata.create_all(bind=database.engine)
context = get_db()


def get_book(name: str) -> Book | None:
    db = SessionLocal()
    return db.query(Book).filter(Book.name == name).first()

def make_book(book: Book) -> Book:
    db = SessionLocal()
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

book = get_book("lol")
print(book)

book2 = Book(
    id = 2,
    name = "yey",
)

make_book(book2)
book = get_book("yey")

app = App()
app.mainloop()
