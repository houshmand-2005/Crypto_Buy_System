from django.contrib.auth.base_user import BaseUserManager
from django.shortcuts import get_object_or_404
import accounts.models.user as user_modul


class UserManager(BaseUserManager):
    def update_password(self, user, new_password):
        user.set_password(new_password)
        user.save()

    def create_user(
        self,
        last_login,
        user_name,
        phone_number,
        password,
        amount,
        is_active,
        is_staff,
        is_superuser,
    ):
        """create user"""
        user = user_modul.User.objects.create(
            last_login=last_login,
            user_name=user_name,
            phone_number=phone_number,
            amount=amount,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, user_name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number, user_name, password, **extra_fields)

    def delete_user(self, user, user_name):
        user_name = get_object_or_404(user, user_name=user_name)
        user_name.delete()

    def update_user(self, user, **data):
        if "password" in data:
            UserManager.update_password(self, user, data["password"])
            del data["password"]
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
