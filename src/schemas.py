# -*- coding: utf-8 -*-
from uuid import uuid4, UUID
from datetime import datetime

from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: UUID

    model_config = {
        'from_attributes' : True
    }

class TokenBase(BaseModel):
    url: str
    username: str
    token: str

class TokenCreate(TokenBase):
    pass

class Token(TokenBase):
    id: UUID

    model_config = {
        'from_attributes' : True
    }

class MarkdownBase(BaseModel):
    desc: str
    markdown: str

class MarkdownCreate(MarkdownBase):
    pass

class Markdown(MarkdownBase):
    id: UUID

    model_config = {
        'from_attributes' : True
    }

class FileBase(BaseModel):
    desc: str
    location: str

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: UUID

    model_config = {
        'from_attributes' : True
    }
