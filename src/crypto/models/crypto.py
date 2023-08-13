from django.db import models, transaction
from utils.models import BaseModel


class CryptoCurrency(BaseModel, models.Model):
    abbreviation = models.CharField(
        "crypto_abbreviation_name", max_length=3, unique=True
    )
    name = models.CharField("crypto_name", max_length=50)
    purchase_price = models.DecimalField(
        "crypto_purchase_price", max_digits=20, decimal_places=5, default=0
    )
    sale_price = models.DecimalField(
        "crypto_sales_price", max_digits=20, decimal_places=5, default=0
    )
    logo = models.ImageField("Crypto logo", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}-{self.abbreviation}"

    @transaction.atomic
    def change_purchase_price(self, price: int) -> int:
        """change the purchase price"""
        self.purchase_price = price
        self.save()
        return self.purchase_price

    @transaction.atomic
    def change_sale_price(self, price: int) -> int:
        """change the sale price"""
        self.sale_price = price
        self.save()
        return self.sale_price
