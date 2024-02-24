import os
from uuid import UUID

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .crud import *
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

BASE_PATH="/api/hicksm/v1"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post(BASE_PATH + "/user", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    item = UserService.read(db=db, filters={'email' : user.email}).first()
    if item:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    return UserService.create(db=db, user=user)

@app.get(BASE_PATH + "/user/{uid}", response_model=schemas.User)
def get_user(uid: UUID, db: Session = Depends(get_db)):
    item = UserService.read(db=db, filters={'id' : uid}).first()
    if not item:
        raise HTTPException(
            status_code=404,
            detail="No such user"
        )
    
    return item

@app.put(BASE_PATH + "/user/{uid}", response_model=schemas.User)
def update_user(uid: UUID, update: user_schema.UserBase, db: Session = Depends(get_db)):
    item = UserService.read(db=db, filters={'email' : update.email}).first()
    if item and item.id != uid:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    return UserService.update(uid=uid, user=update, db=db)

@app.delete(BASE_PATH + "/user/{uid}", response_model=schemas.User)
def post_user(uid: UUID, update: user_schema.UserBase, db: Session = Depends(get_db)):
    item = get_user(uid=uid, db=db)

    return UserService.delete(db=db, uid=uid)

@app.post(BASE_PATH + "/token", response_model=schemas.Token)
def upload_token(token: schemas.TokenCreate, db: Session = Depends(get_db)):
    item = TokenService.read(db=db, filters=token.dict()).first()
    if item:
        raise HTTPException(
            status_code=400,
            detail="Token already exists"
        )

    return TokenService.create(db=db, token=token)

@app.get(BASE_PATH + "/tokens", response_model=List[schemas.Token])
def get_tokens(db: Session = Depends(get_db)):
    return TokenService.read(db=db)

@app.get(BASE_PATH + "/token/{uid}", response_model=schemas.Token)
def get_token(uid: UUID, db: Session = Depends(get_db)):
    item = TokenService.read(db=db, filters={'id' : uid}).first()
    if not item:
        raise HTTPException(
            status_code=404,
            detail="Token does not exist"
        )

    return item

@app.put(BASE_PATH + "/token/{uid}", response_model=schemas.Token)
def update_token(uid: UUID, update: user_schema.TokenUpdate, db: Session = Depends(get_db)):
    item = TokenService.read(db=db, filters={
        'url' : update.url,
        'username' : update.username,
        'token' : update.token
    }).first()
    if item:
        raise HTTPException(
            status_code=400,
            detail="Matching token already exists"
        )
    
    return TokenService.update(uid=uid, token=update, db=db)

@app.delete(BASE_PATH + "/token/{uid}", response_model=schemas.Token)
def delete_token(uid: UUID, db: Session = Depends(get_db)):
    item = get_user(uid=uid, db=db)

    return TokenService.delete(uid=uid, db=db)

@app.post(BASE_PATH + "/markdown", response_model=schemas.Markdown)
def upload_markdown(markdown: schemas.MarkdownCreate, db: Session = Depends(get_db)):
    item = MarkdownService.read(db=db, filters={'desc' : markdown.desc}).first()
    if item:
        raise HTTPException(
            status_code=400,
            detail="Markdown already exists"
        )
    
    return MarkdownSerivce.create(db=db, token=token)

@app.get(BASE_PATH + "/markdown/{desc}", response_model=schemas.Markdown)
def get_markdown(desc: str, db: Session = Depends(get_db)):
    item = MarkdownService.read(db=db, filters={'desc' : desc}).first()
    if not item:
        raise HTTPException(
            status_code=404,
            detail="Markdown does not exist"
        )
    
    return item

@app.put(BASE_PATH + "/markdown/{desc}", response_model=schemas.Markdown)
def update_markdown(desc: str, markdown: str, db: Session = Depends(get_db)):
    item = get_markdown(desc=desc, db=db)

    return MarkdownService.update(uid=item.id, markdown=MarkdownBase(desc=desc, markdown=markdown), db=db)

@app.post(BASE_PATH + "/file", response_model=schemas.File)
def upload_file(file: schemas.FileCreate, contents: str, db: Session = Depends(get_db)):
    item = FileService.read(db=db, filters={'location' : file.location}).first()
    if item:
        raise HTTPException(
            status_code=400,
            detail="File at input path already exists"
        )
    
    os.system(f"echo \"{contents}\" > {file.location}")
    
    return FileService.create(db=db, token=token)

@app.get(BASE_PATH + "/files", response_model=List[schemas.File])
def get_files(db: Session = Depends(get_db)):
    return FileService.get(db=db)

@app.get(BASE_PATH + "/files/{uid}", response_model=schemas.File)
def get_file(uid: UUID, db: Session = Depends(get_db)):
    item = FileService.read(db=db, filters={'id' : uid}).first()
    if not item:
        raise HTTPException(
            status_code=404,
            detail="File does not exist"
        )
    
    return item

@app.get(BASE_PATH + "/files/{uid}/contents")
def get_file_contents(uid: UUID, db: Session = Depends(get_db)):
    item = get_file(uid=uid, db=db)

    contents = None
    with open(item.location, "r") as f:
        contents = {
            'status' : 200,
            'message' : f.read()
        }

    if not contents:
        contents = {
            'status' : 500,
            'message' : "Could not read file contents."
        }
        
    return contents

@app.put(BASE_PATH + "/files/{uid}", response_model=schemas.File)
def update_file(uid: UUID, contents: str, update: schemas.FileUpdate, db: Session = Depends(get_db)):
    item = get_file(uid=uid, db=db)

    os.system(f"rm {item.location}")
    os.system(f"echo \"{contents}\" > {update.location}")

    return FileService.update(db=db, uid=uid, file=update)
