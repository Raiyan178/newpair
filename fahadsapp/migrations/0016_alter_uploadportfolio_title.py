# Generated by Django 4.0.1 on 2022-01-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahadsapp', '0015_alter_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadportfolio',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]