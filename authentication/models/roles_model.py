from django.db import models
from .Base_model import TimeStampedModel


class Role(models.Model):
    role_code = models.CharField(max_length=100, unique=True)
    role_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = "Role"