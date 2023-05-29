from tortoise import fields, models


class Message(models.Model):
    created_at = fields.TextField()
    payload = fields.TextField()

    class Meta:
        ordering = ["-created_at"]