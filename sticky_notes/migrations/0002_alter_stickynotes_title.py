# Generated by Django 5.0.6 on 2024-06-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sticky_notes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stickynotes",
            name="title",
            field=models.CharField(max_length=22),
        ),
    ]
