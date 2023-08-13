from django.db import models
from utils.models import BaseModel
from accounts.models.user import User
from crypto.models.crypto import CryptoCurrency


class Transactions(BaseModel, models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    crypto_currency = models.ForeignKey(
        CryptoCurrency,
        on_delete=models.DO_NOTHING,
        null=True,
    )
    new_amount = models.DecimalField(
        "new_amount", max_digits=20, decimal_places=5, default=0
    )
    before_amount = models.DecimalField(
        "before_amount", max_digits=20, decimal_places=5, default=0
    )
    note = models.CharField("note", max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user}-{self.crypto_currency}-{self.new_amount}"
