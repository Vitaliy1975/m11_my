from datetime import date
from pydantic import BaseModel, Field,EmailStr


class ContactModel(BaseModel):
    first_name:str=Field(min_length=2,max_length=25)
    last_name:str=Field(min_length=2,max_length=25)
    email:EmailStr
    phone_number:int=Field()
    birthday:date
    additional_data:str=Field(max_length=255)

    class Config:
        orm_mode=True


class ContactResponse(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:EmailStr
    phone_number:int
    birthday:date
    additional_data:str

    class Config:
        orm_mode=True
