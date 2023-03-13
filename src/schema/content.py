from typing import Text, Optional
from datetime import datetime


class Content:
    def __init__(self, endpoint: str, name: str, slug: str, content: Text, created_at: datetime,
                 updated_at: datetime, is_active: bool, id: Optional[int] = None) -> None:
        self.id = id
        self.endpoint = endpoint
        self.name = name
        self.slug = slug
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active
