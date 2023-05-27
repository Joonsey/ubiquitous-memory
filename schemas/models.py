from __future__ import annotations
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column
from schemas.database import Base

class Student(Base):
    __tablename__ = "students"

    number = mapped_column(Integer, primary_key=True)
    firstname = Column(String(80))
    lastname = Column(String(80))

class Course(Base):
    __tablename__ = "courses"

    code = mapped_column(String(50), primary_key=True)
    name = Column(String(80), nullable=False)
    points = Column(Integer)

class Book(Base):
    __tablename__ = "books"

    id = Column(String(80), primary_key=True)
    name = Column(String(50))
    subject = Column(String(50))
    student_number = Column(ForeignKey(Student.number), primary_key=True, nullable=True)
    date = Column(Date, nullable=True)


class Reader(Base):
    __tablename__ = "readers"

    student_number  = Column(ForeignKey(Student.number), primary_key=True)
    course_code = Column(ForeignKey(Course.code), primary_key=True)
