from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]






#models for sqlite database
# from .database import Base

# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

# class Blog(Base):
#     __tablename__ = "blog"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     body = Column(String)
#     published = Column(Boolean, default=True)