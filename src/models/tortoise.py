from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Message(models.Model):
    created_at = fields.TextField()
    payload = fields.TextField()


MessageSchema = pydantic_model_creator(Message, exclude=("id",))
