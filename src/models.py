# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

_TARGET_LENGTH = 6

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

class Session(Base):
    __tablename__ = "session"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    email: Mapped[str]
    creation_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    accessed_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))

class Challenge(Base):
    __tablename__ = "challenge"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    creation_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    target: Mapped[str] = mapped_column(String(_TARGET_LENGTH))
    code_to_eval: Mapped[Optional[str]]
