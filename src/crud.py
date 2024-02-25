# -*- coding: utf-8 -*-
from uuid import UUID
from copy import deepcopy
from datetime import datetime

from sqlalchemy import asc
from sqlalchemy.orm import Session

from . import models, schemas

class UserService:

    @staticmethod
    def create(db: Session, user: schemas.UserCreate):
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
    def create(db: Session, token: schemas.TokenCreate):
        item = models.Token(
            id=get_uuid(tbl=models.Token, db=db),
            **token.dict(),
            active=True
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
    def update(db: Session, uid: UUID, token: schemas.TokenUpdate):
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
    def create(db: Session, markdown: schemas.MarkdownCreate):
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
    def create(db: Session, file: schemas.FileCreate):
        item = models.File(
            id=get_uuid(tbl=models.File, db=db),
            **file.dict(),
            page=None
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
    def update(db: Session, uid: UUID, file: schemas.FileUpdate):
        item = FileService.read(db=db, filters={'id' : uid}).first()

        for key, value in file.dict():
            setattr(item, key, value)
        
        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def delete(db: Session, uid: UUID):
        item = FileService.read(db=db, filters={'id' : uid})

        item_copy = deepcopy(item.first())

        item.delete()
        db.commit()

        return item_copy

class ChallengeService:

    @staticmethod
    def create(db: Session, code_to_eval: str):
        challenges = list(ChallengeService.read(db=db).all())
        if len(challenges) == models._MAX_CHALLENGES:
            oldest = ChallengeService.read(db=db).order_by(asc('creation_time')).limit(1)
            ChallengeService.delete(db=db, uid=oldest.id)

        challenge = models.Challenge(
            id=get_uuid(tbl=models.Challenge, db=db),
            creation_time=datetime.now(),
            target=''.join(random.choices(string.ascii_letters + string.digits, k=models._TARGET_LENGTH)),
            code_to_eval=code_to_eval
        )

        db.add(challenge)
        db.commit()

        return challenge

    @staticmethod
    def read(db: Session, filters: dict[str, Any] = None):
        items = db.query(models.Challenge)
        if filters:
            items.filter_by(**filters)
        
        return items
    
    @staticmethod
    def delete(db: Session, uid: UUID):
        item = ChallengeService.read(db=db, filters={'id' : uid})

        item_copy = deepcopy(item.first())

        item.delete()
        db.commit()

        return item_copy

class SessionService:

    @staticmethod
    def create(db: Session, request: schemas.SessionCreate):
        sessions = list(SessionService.read(db=db).all())
        if len(sessions) == models._MAX_SESSIONS:
            oldest = SessionService.read(db=db).order_by(asc('creation_time')).limit(1)
            SessionService.delete(db=db, uid=oldest.id)
        
        session = models.Session(
            id=get_uuid(tbl=models.Session, db=db),
            email=request.email,
            creation_time=datetime.now(),
            accessed_time=datetime.now()
        )

        db.add(session)
        db.commit()

        return session
    
    @staticmethod
    def read(db: Session, filters: dict[str, Any] = None):
        items = db.query(models.Session)
        if filters:
            items.filter_by(**filters)
        
        return items
    
    @staticmethod
    def update(db: Session, uid: UUID, session: schemas.SessionUpdate):
        item = SessionService.read(db=db, filters={'id' : uid}).first()

        for key, value in session.dict():
            setattr(item, key, value)
        
        db.commit()
        db.refresh(item)

        return item
    
    @staticmethod
    def delete(db: Session, uid: UUID):
        item = SessionService.read(db=db, filters={'id' : uid})

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
