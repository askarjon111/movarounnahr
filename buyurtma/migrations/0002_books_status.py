# Generated by Django 3.1.7 on 2021-04-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
