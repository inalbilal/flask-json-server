from typing import Type
from sqlalchemy.orm import Session
from src.entity.content import Content


class ContentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, content: Content) -> Content:
        self.session.add(content)
        self.session.commit()
        self.session.refresh(content)
        return content

    def update(self, content: Content) -> Content:
        self.session.commit()
        self.session.refresh(content)
        return content

    def delete(self, content: Content) -> None:
        self.session.delete(content)
        self.session.commit()

    def get_by_id(self, content_id: int) -> Content:
        return self.session.query(Content).get(content_id)

    def get_by_slug(self, content_slug: str) -> Content | None:
        return self.session.query(Content).filter_by(slug=content_slug).first()

    def get_by_content_ep(self, content_slug: str, content_endpoint: str) -> Content | None:
        return self.session.query(Content).filter_by(endpoint=content_endpoint, slug=content_slug).first()

    def get_all(self) -> list[Type[Content]]:
        return self.session.query(Content).all()
