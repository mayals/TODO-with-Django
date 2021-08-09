# Generated by Django 3.2.5 on 2021-08-07 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='P_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='U_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]