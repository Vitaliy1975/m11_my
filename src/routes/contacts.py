from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactModel,ContactResponse
from src.repository import contacts as repository_contacts
router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get("/", response_model=List[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = await repository_contacts.get_contacts(skip, limit, db)
    return tags


@router.get("/{tag_id}", response_model=ContactResponse)
async def read_contact(tag_id: int, db: Session = Depends(get_db)):
    tag = await repository_contacts.get_contact(tag_id, db)
    if tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return tag


@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(body, db)


@router.put("/{tag_id}", response_model=ContactResponse)
async def update_contact(body: ContactModel, tag_id: int, db: Session = Depends(get_db)):
    tag = await repository_contacts.update_contact(tag_id, body, db)
    if tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return tag


@router.delete("/{tag_id}", response_model=ContactResponse)
async def remove_contact(tag_id: int, db: Session = Depends(get_db)):
    tag = await repository_contacts.remove_contact(tag_id, db)
    if tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return tag


@router.get("/find/",response_model=List[ContactResponse])
async def find_contacts(first_name:str=None,last_name:str=None,email:str=None,db:Session=Depends(get_db)):
    result=await repository_contacts.search_contacts(db,first_name,last_name,email)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Contact not found")
    return result


@router.get("/birthday/",response_model=List[ContactResponse])
async def birth_contacts(db:Session=Depends(get_db)):
    result=await repository_contacts.birthdays(db)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Contact not found")
    return result