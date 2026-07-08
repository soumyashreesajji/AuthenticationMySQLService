from django.db import models
from .roles_model import Role
from .permissions_model import Permission

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="permissions")
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        db_table = "RolePermissions"
        unique_together = ('role', 'permission')
        