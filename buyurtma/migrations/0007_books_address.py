# Generated by Django 3.1.7 on 2021-06-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0006_auto_20210615_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
