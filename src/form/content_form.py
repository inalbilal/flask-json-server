from wtforms import Form, StringField, validators, TextAreaField
from wtforms.validators import InputRequired
from src.validator.wtforms.validate import Validate


class ContentForm(Form):
    endpoint = StringField(label="", validators=[validators.Length(min=1, max=255)])
    name = StringField(label="", validators=[validators.Length(min=1, max=255)])
    content = TextAreaField(label="", validators=[InputRequired(), Validate.validate_json])
