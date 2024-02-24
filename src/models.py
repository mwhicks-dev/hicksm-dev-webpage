# -*- coding: utf-8 -*-

from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    administrator: Mapped[bool]

class Token(Base):
    __tablename__ = "tokens"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    url: Mapped[str]
    username: Mapped[str]
    token: Mapped[str]
    active: Mapped[bool]

class Markdown(Base):
    __tablename__ = "markdowns"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    desc: Mapped[str]
    markdown: Mapped[str]

class File(Base):
    __tablename__ = "files"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    desc: Mapped[str]
    location: Mapped[str]
    data_type: Mapped[Optional[str]]
