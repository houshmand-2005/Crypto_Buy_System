# Generated by Django 4.2.4 on 2023-08-12 18:20

from django.conf import settings
import django.contrib.auth.password_validation
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utils.create_random_wallet
import utils.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crypto', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('user_name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(5), utils.validators.username_validator], verbose_name='user_name')),
                ('phone_number', models.CharField(max_length=20, unique=True, validators=[utils.validators.phone_validator], verbose_name='phone_number')),
                ('password', models.CharField(max_length=128, validators=[django.contrib.auth.password_validation.validate_password], verbose_name='password')),
                ('amount', models.DecimalField(decimal_places=5, default=0, max_digits=20, verbose_name='user_amount_real_mony')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='uuid')),
                ('amount', models.DecimalField(decimal_places=5, default=0, max_digits=20, verbose_name='user_amount')),
                ('wallet_address', models.CharField(default=utils.create_random_wallet.create_wallet_crypto, max_length=100, unique=True)),
                ('crypto_currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crypto.cryptocurrency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='wallet',
            constraint=models.UniqueConstraint(fields=('user', 'crypto_currency'), name='unique_user_currency'),
        ),
    ]
