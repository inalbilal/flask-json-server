import json

from wtforms import ValidationError, Field


class Validate:
    def validate_json(self, field: Field) -> None:
        try:
            json.loads(field.data)
        except ValueError:
            raise ValidationError("Invalid JSON")
