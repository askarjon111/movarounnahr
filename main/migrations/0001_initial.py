# Generated by Django 3.1.7 on 2021-04-23 09:58

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xlsx', models.FileField(upload_to='template')),
            ],
            options={
                'verbose_name_plural': 'Excel',
            },
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sotuv Transkript',
            },
        ),
        migrations.CreateModel(
            name='ObjectionWrite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objection', models.TextField()),
                ('solution', models.TextField()),
                ('create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Mijoz e`tirozlari',
            },
        ),
        migrations.CreateModel(
            name='Objections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objection', models.TextField()),
                ('solution', models.TextField()),
                ('create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Ko`p takrorlanadigan e`tirozlar',
            },
        ),
        migrations.CreateModel(
            name='Debtors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('debt', models.BooleanField()),
                ('create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.lead')),
            ],
            options={
                'verbose_name_plural': 'Qarzdorliklar',
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('bg-primary', "Ko'k"), ('bg-warning', 'Sariq'), ('bg-info', 'Fiolet'), ('bg-success', 'Yashil'), ('bg-danger', 'Qizil')], default='bg-primary', max_length=255)),
                ('event', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.lead')),
            ],
            options={
                'verbose_name_plural': 'Kalendar',
            },
        ),
    ]
