from django.db import models
from .users_model import User
from .roles_model import Role


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_roles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role_users")
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="role_assigned_by", null=True)
    assigned_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "User_Roles"
        unique_together = ("user", "role")
