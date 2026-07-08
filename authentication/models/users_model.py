from .Base_model import TimeStampedModel
from django.db import models


class User(TimeStampedModel):
    person_id = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Reference to Person Service person_id"
    )
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='active')
    email_verified = models.BooleanField(default=False)
    otp_login_enabled = models.BooleanField(default=True)
    last_login_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Users"
        indexes = [
            models.Index(fields=['person_id']),
            models.Index(fields=['username']),
            models.Index(fields=['email'])
        ]