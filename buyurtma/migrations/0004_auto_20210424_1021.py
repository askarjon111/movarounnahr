# Generated by Django 3.1.7 on 2021-04-24 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_filial_bot_token'),
        ('buyurtma', '0003_auto_20210424_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='filial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.filial'),
        ),
    ]