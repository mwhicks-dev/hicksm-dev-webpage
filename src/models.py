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
    creation_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    updated_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    administrator: Mapped[bool]

class Token(Base):
    __tablename__ = "tokens"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    url: Mapped[str]
    username: Mapped[str]
    token: Mapped[str]

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
