from sqlalchemy import Column, Integer, String, Boolean, func, Table
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# note_m2m_tag = Table(
#     "note_m2m_tag",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("note_id", Integer, ForeignKey("notes.id", ondelete="CASCADE")),
#     Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE")),
# )


# class Note(Base):
#     __tablename__ = "notes"
#     id = Column(Integer, primary_key=True)
#     title = Column(String(50), nullable=False)
    # created_at = Column('created_at', DateTime, default=func.now())
#     description = Column(String(150), nullable=False)
#     done = Column(Boolean, default=False)
#     tags = relationship("Tag", secondary=note_m2m_tag, backref="notes")


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name=Column(String(25),nullable=False)
    email=Column(String(125),unique=True)
    phone_number=Column(Integer,unique=True)
    birthday=Column("birthday",Date)
    additional_data=Column(String(255))