from django.db import models


class Permission(models.Model):
    permission_code = models.CharField(max_length=100, unique=True)
    permission_name = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.permission_name

    class Meta:
        db_table = "Permissions"

        