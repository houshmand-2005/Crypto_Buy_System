from django.contrib import admin
from accounts.models.user import User
from accounts.models.wallet import Wallet


class UserAdmin(admin.ModelAdmin):
    """User admin class for user model in admin panel"""

    list_display = (
        "id",
        "user_name",
        "is_active",
        "is_staff",
        "amount",
        "update_at",
    )
    search_fields = ("user_name",)

    list_filter = (
        "is_active",
        "is_staff",
    )


class WalletAdmin(admin.ModelAdmin):
    """Wallet admin for wallet model in admin panel for showing more data"""

    list_display = (
        "uuid",
        "user",
        "amount",
        "created_at",
    )
    search_fields = ("user",)


admin.site.register(User, UserAdmin)
admin.site.register(Wallet, WalletAdmin)
