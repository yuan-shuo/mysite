# Generated by Django 4.1 on 2024-02-12 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0003_onlytitle"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userinfo",
            name="nothing",
        ),
        migrations.RemoveField(
            model_name="userinfo",
            name="title",
        ),
    ]
