from src.schema.content import Content as ContentSchema
from src.entity.content import Content


class ContentBuilder:
    def buildFromEntity(self: Content) -> ContentSchema:
        return ContentSchema(
            id=self.id,
            endpoint=self.endpoint,
            name=self.name,
            slug=self.slug,
            content=self.content,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_active=self.is_active
        )
