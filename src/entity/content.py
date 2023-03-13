from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from . import Base


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    endpoint = Column(String(255))
    name = Column(String(255))
    slug = Column(String(255))
    content = Column(Text())
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
    is_active = Column(Boolean())

    def __repr__(self) -> str:
        return f"Name={self.name!r}"
