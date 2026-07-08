from django.db import models
from .users_model import User


class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="login_history")
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, null=True)
    login_status = models.CharField(max_length=50)

    class Meta:
        db_table = "login_history"