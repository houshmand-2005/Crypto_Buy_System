from django.contrib import admin
from transactions.models.transaction import Transactions


class TransactionsAdmin(admin.ModelAdmin):
    """TransactionsAdmin admin class for CryptoCurrencies model in admin panel"""

    list_display = (
        "id",
        "new_amount",
        "before_amount",
        "user",
        "note",
    )
    search_fields = ("user", "note")


admin.site.register(Transactions, TransactionsAdmin)
