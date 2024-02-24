# -*- coding: utf-8 -*-
from uuid import UUID
from copy import deepcopy

from sqlalchemy.orm import Session

from . import models, schemas

class UserService:

    @staticmethod
    def create(db: Session, user: schemas.UserDto):
        item = models.User(
            id=get_uuid(tbl=models.User, db=db),
            **user.dict(),
            administrator=False
        )

        db.add(item)
        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def read(db: Session, filters: dict[str, Any] = None):
        items = db.query(models.User)
        if filters:
            items.filter_by(**filters)
        
        return items
    
    @staticmethod
    def update(db: Session, uid: UUID, user: schemas.UserBase):
        item = UserService.read(db=db, filters={'id' : uid}).first()

        for key, value in user.dict():
            setattr(item, key, value)
        
        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def delete(db: Session, uid: UUID):
        item = UserService.read(db=db, filters={'id' : uid})

        item_copy = deepcopy(item.first())

        item.delete()
        db.commit()

        return item_copy

class TokenService:

    @staticmethod
    def create(db: Session, token: schemas.TokenDto):
        item = models.Token(
            id=get_uuid(tbl=models.Token, db=db),
            **token.dict()
        )

        db.add(item)
        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def read(db: Session, filters: dict[str, Any] = None):
        items = db.query(model.Token)
        if filters:
            items.filter_by(**filters)
        
        return items
    
    @staticmethod
    def update(db: Session, uid: UUID, token: schemas.TokenBase):
        item = TokenService.read(db=db, filters={'id' : uid}).first()

        for key, value in token.dict():
            setattr(item, key, value)

        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def delete(db: Session, uid: UUID):
        item = TokenService.read(db=db, filters={'id': uid})

        item_copy = deepcopy(item.first())

        item.delete()
        db.commit()

        return item_copy

class MarkdownService:

    @staticmethod
    def create(db: Session, markdown: schemas.MarkdownDto):
        item = models.Markdown(
            id=get_uuid(tbl=models.Markdown, db=db),
            **markdown.dict()
        )

        db.add(item)
        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def read(db: Session, filters: dict[str, Any] = None):
        items = db.query(models.Markdown)
        if filters:
            items.filter_by(**filters)
        
        return items
    
    @staticmethod
    def update(db: Session, uid: UUID, markdown: schemas.MarkdownBase):
        item = MarkdownService.read(db=db, filters={'id' : uid}).first()
        
        for key, value in markdown.dict():
            setattr(item, key, value)
        
        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def delete(db: Session, uid: UUID):
        item = MarkdownService.read(db=db, filters={'id' : uid})

        item_copy = deepcopy(item.first())

        item.delete()
        db.commit()

        return item_copy

class FileService:

    @staticmethod
    def create(db: Session, file: schemas.FileDto):
        item = models.File(
            id=get_uuid(tbl=models.File, db=db),
            **file.dict()
        )

        db.add(item)
        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def read(db: Session, filters: dict[str, Any] = None):
        items = db.query(models.File)
        if filters:
            items.filter_by(**filters)
        
        return items
    
    @staticmethod
    def update(db: Session, uid: UUID, file: schemas.FileBase):
        item = FileService.read(db=db, filters={'id' : uid}).first()

        for key, value in user.dict():
            setattr(item, key, value)
        
        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def delete(db: Session, uid: UUID):
        item = UserService.read(db=db, filters={'id' : uid})

        item_copy = deepcopy(item.first())

        item.delete()
        db.commit()

        return item_copy

def get_uuid(tbl, db: Session) -> UUID:
    uid = uuid4()

    collision = (
        db.query(tbl)
        .filter(tbl.id == uid)
        .first()
    )

    if collision is None:
        return uid
    else:
        return get_uuid(tbl=tbl, db=db)
