# Generated by Django 4.2.5 on 2023-11-16 07:01

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
            name='UsersProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_id', models.CharField(max_length=10, unique=True)),
                ('dob', models.DateField()),
                ('contact', models.CharField(max_length=13)),
                ('sex', models.CharField(max_length=1)),
                ('nin', models.CharField(max_length=14, unique=True)),
                ('position', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('parish', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
