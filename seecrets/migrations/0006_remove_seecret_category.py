# Generated by Django 3.2.25 on 2024-04-18 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seecrets', '0005_alter_seecret_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seecret',
            name='category',
        ),
    ]
