from django.db import models
from .users_model import User

class OTPRequest(models.Model):
    OTP_PURPOSES = (
        ("LOGIN", "Login"),
        ("EMAIL_VERIFICATION", "Email Verification"),
        ("PASSWORD_RESET", "Password Reset"),
        ("MFA", "Multi Factor Authentication"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="otp_requests")
    email = models.EmailField()
    otp_code = models.CharField(max_length=10)
    purpose = models.CharField(max_length=30, choices=OTP_PURPOSES)
    expires_at = models.DateTimeField()
    verified = models.BooleanField(default=False)
    attempt_count = models.PositiveIntegerField(default=0)
    max_attempts = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "otp_requests"
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["purpose"]),
            models.Index(fields=["verified"]),
        ]

