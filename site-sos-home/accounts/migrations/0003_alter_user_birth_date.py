# Generated by Django 4.1.3 on 2022-11-30 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_birth_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(
                auto_now_add=True, verbose_name="Data de Nascimento"
            ),
        ),
    ]
