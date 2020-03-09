from uuid import uuid4


from django.db import models


class File(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    file = models.FileField(
    )

    explanation = models.CharField(
        max_length=300,
        blank=False,
        null=False,
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
