from datetime import datetime
from slugify import slugify
from src.form.content_form import ContentForm
from src.schema.content import Content


class ContentParser:
    @staticmethod
    def parse(request_data: ContentForm) -> Content:
        return Content(
            endpoint=request_data.endpoint.data,
            name=request_data.name.data,
            slug=slugify(request_data.name.data),
            content=request_data.content.data,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            is_active=True
        )
