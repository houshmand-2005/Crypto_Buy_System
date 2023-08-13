from django.contrib import admin
from crypto.models.crypto import CryptoCurrency


class CryptoCurrencyAdmin(admin.ModelAdmin):
    """ryptoCurrency admin class for CryptoCurrencies model in admin panel"""

    list_display = (
        "id",
        "abbreviation",
        "name",
        "purchase_price",
        "sale_price",
    )
    search_fields = ("abbreviation", "name")


admin.site.register(CryptoCurrency, CryptoCurrencyAdmin)
