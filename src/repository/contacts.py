from typing import List
import datetime

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(tag_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == tag_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    tag = Contact(first_name=body.first_name,last_name=body.last_name,email=body.email,phone_number=body.phone_number,birthday=body.birthday,additional_data=body.additional_data)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


async def update_contact(tag_id: int, body: ContactModel, db: Session) -> Contact | None:
    tag = db.query(Contact).filter(Contact.id == tag_id).first()
    if tag:
        tag.first_name = body.first_name
        tag.last_name=body.last_name
        tag.email=body.email
        tag.phone_number=body.phone_number
        tag.birthday=body.birthday
        tag.additional_data=body.additional_data
        db.commit()
    return tag


async def remove_contact(tag_id: int, db: Session)  -> Contact | None:
    tag = db.query(Contact).filter(Contact.id == tag_id).first()
    if tag:
        db.delete(tag)
        db.commit()
    return tag


async def search_contacts(db: Session, first_name: str = None, last_name: str = None, email: str = None):
    if first_name and last_name and email:
        return db.query(Contact).filter(Contact.first_name == first_name,Contact.last_name == last_name,Contact.email == email).all()
    elif first_name and last_name:
        return db.query(Contact).filter(Contact.first_name == first_name,Contact.last_name == last_name).all()
    elif last_name and email:
        return db.query(Contact).filter(Contact.last_name == last_name,Contact.email == email).all()
    elif first_name and email:
        return db.query(Contact).filter(Contact.first_name == first_name,Contact.email == email).all()
    elif first_name:
        return db.query(Contact).filter(Contact.first_name == first_name).all()
    elif last_name:
        return db.query(Contact).filter(Contact.last_name == last_name).all()
    elif email:
        return db.query(Contact).filter(Contact.email == email).all()
    return None


async def birthdays(db: Session):
        contacts=db.query(Contact).all()
        congratulation_list=[]
        today_date=datetime.datetime.today().date()
        today_year=today_date.year
        today_year_string=str(today_year)
        for contact in contacts:
            birthday_noyear_string=(contact.birthday).strftime("%m.%d")
            birthday_this_year_string=today_year_string+"."+birthday_noyear_string
            birthday_this_year=datetime.datetime.strptime(birthday_this_year_string,"%Y.%m.%d").date()
            difference=birthday_this_year-today_date
            if difference.days<0:
                continue
            elif difference.days>7:
                continue
            else:
                congratulation_list.append(contact)
        return congratulation_list