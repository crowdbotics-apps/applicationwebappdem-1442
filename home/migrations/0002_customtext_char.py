# Generated by Django 2.2.9 on 2020-01-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="char",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
