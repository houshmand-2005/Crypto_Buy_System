from django.db import models, transaction
from django.core.validators import MinLengthValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from utils.models import BaseModel
from utils.validators import phone_validator, username_validator
from accounts.managers.user_manager import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(
        "user_name",
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(5), username_validator],
    )
    phone_number = models.CharField(
        "phone_number",
        validators=[phone_validator],
        max_length=20,
        unique=True,
    )
    password = models.CharField(
        "password",
        max_length=128,
        validators=[validate_password],
    )
    amount = models.DecimalField(
        "user_amount_real_mony", max_digits=20, decimal_places=5, default=0
    )
    is_active = models.BooleanField("active", default=True)
    is_staff = models.BooleanField("is staff", default=False)

    objects = UserManager()
    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["phone_number"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return f"{self.phone_number} - {self.user_name}"

    @transaction.atomic
    def charge_wallet(self, amount: int) -> int:
        """Charging user wallet. increasing wallet amount."""
        self.amount += amount
        self.save()
        return self.amount

    @transaction.atomic
    def decreasing_wallet(self, amount: int) -> int:
        """decreasing wallet amount."""
        self.amount -= amount
        self.save()
        return self.amount
