# Generated by Django 3.2 on 2021-05-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0002_auto_20210506_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='supplier_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='supplier_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
