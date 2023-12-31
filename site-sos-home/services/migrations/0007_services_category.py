# Generated by Django 4.1.3 on 2022-12-04 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
        ("services", "0006_alter_services_job_date_alter_services_job_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="services",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="pages.category",
            ),
            preserve_default=False,
        ),
    ]
