from flask import abort
from sqlalchemy.orm import Session
from src.builder.entity.content_builder import ContentBuilder
from src.builder.schema.content_builder import ContentBuilder as ContentSchemaBuilder
from src.entity import Base
from src.schema.content import Content as ContentSchema
from src.form.content_form import ContentForm
from src.parser.content_parser import ContentParser
from src.repository.content_repositroy import ContentRepository
from src.trait.sqlalchemy_engine import OrmEngine


class JsonServerService:
    def __init__(self):
        self.orm_engine = OrmEngine()
        self.content_parser = ContentParser()

    def create_json_server(self, form: ContentForm) -> ContentSchema:
        session = Session(self.orm_engine.engine)

        Base.metadata.create_all(self.orm_engine.engine)

        content = self.content_parser.parse(form)
        content_entity = ContentBuilder.buildFromSchema(content)
        content_schema = ContentSchemaBuilder.buildFromEntity(content_entity)
        content_repository = ContentRepository(session)
        content_repository.create(content_entity)

        return content_schema

    def load_json_server(self, slug: str, endpoint: str) -> ContentSchema:
        session = Session(self.orm_engine.engine)
        content_repository = ContentRepository(session)
        content = content_repository.get_by_content_ep(slug, endpoint)
        if content is None:
            abort(404)

        content_schema = ContentSchemaBuilder.buildFromEntity(content)

        return content_schema
