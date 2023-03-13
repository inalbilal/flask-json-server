from src.schema.content import Content
from src.entity.content import Content as ContentEntity


class ContentBuilder:
    def buildFromSchema(self: Content) -> ContentEntity:
        return ContentEntity(
            id=self.id,
            endpoint=self.endpoint,
            name=self.name,
            slug=self.slug,
            content=self.content,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_active=self.is_active
        )
