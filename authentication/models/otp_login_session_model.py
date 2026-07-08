from django.db import models
from .users_model import User
from .otp_request_model import OTPRequest

class OTPLoginSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_request = models.ForeignKey(OTPRequest, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device_info = models.TextField(null=True, blank=True)
    session_identifier = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "otp_login_sessions"