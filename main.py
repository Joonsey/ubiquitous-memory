#import tkinter

from schemas import database
from schemas.database import SessionLocal, get_db
from schemas.models import Book
from sqlalchemy.orm import Session

database.Base.metadata.create_all(bind=database.engine)
context = get_db()


def get_book(db: Session, name: str) -> Book | None:
    return db.query(Book).filter(Book.name == name).first()

def make_book(db: Session, book: Book) -> Book | None:
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

book = get_book(SessionLocal(), "lol")
print(book)

book2 = Book(
    id = 2,
    name = "yey",
)

make_book(SessionLocal(), book2)

book = get_book(SessionLocal(), "yey")
print(book)
