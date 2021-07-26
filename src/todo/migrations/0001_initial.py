# Generated by Django 3.2.5 on 2021-07-26 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_name', models.CharField(max_length=60)),
                ('T_status', models.BooleanField(default=False)),
                ('T_published', models.DateTimeField(auto_now_add=True)),
                ('T_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='U_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-T_published',),
            },
        ),
    ]
