# Generated by Django 4.2.3 on 2023-07-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("todo", models.CharField(max_length=10000)),
                ("created_on", models.DateField(auto_now_add=True)),
                ("is_completed", models.BooleanField(default=False)),
            ],
        ),
    ]