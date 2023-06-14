from tortoise import fields, models


class Message(models.Model):
    created_at = fields.DatetimeField()
    payload = fields.JSONField()

    class Meta:
        ordering = ["-created_at"]
