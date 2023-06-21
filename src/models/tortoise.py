from typing import ClassVar

from tortoise import fields, models


class Message(models.Model):
    created_at = fields.DatetimeField()
    payload = fields.JSONField()

    class Meta:
        ordering: ClassVar[list[str]] = ["-created_at"]
