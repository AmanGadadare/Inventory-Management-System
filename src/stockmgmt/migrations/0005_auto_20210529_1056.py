# Generated by Django 3.2 on 2021-05-29 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0004_auto_20210529_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='supplier_name',
        ),
        migrations.RemoveField(
            model_name='stockhistory',
            name='supplier_name',
        ),
    ]
