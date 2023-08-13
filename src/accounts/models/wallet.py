import uuid
from django.db import models, transaction
from django.db.models import UniqueConstraint
from utils.models import BaseModel
from accounts.models.user import User
from crypto.models.crypto import CryptoCurrency
from utils.create_random_wallet import create_wallet_crypto


class Wallet(BaseModel):
    uuid = models.UUIDField(
        "uuid",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    user = models.ForeignKey(
        User,
        related_name="wallet",
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        "user_amount", max_digits=20, decimal_places=5, default=0
    )
    crypto_currency = models.ForeignKey(
        CryptoCurrency,
        on_delete=models.DO_NOTHING,
        null=True,
    )
    wallet_address = models.CharField(
        max_length=100, default=create_wallet_crypto, unique=True
    )

    def __str__(self) -> str:
        return f"{self.user.user_name} - {self.crypto_currency} - {self.amount}"

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

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["user", "crypto_currency"], name="unique_user_currency"
            )
        ]
