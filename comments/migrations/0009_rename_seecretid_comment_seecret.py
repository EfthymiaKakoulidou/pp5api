# Generated by Django 3.2.25 on 2024-04-09 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_rename_seecret_comment_seecretid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='seecretid',
            new_name='seecret',
        ),
    ]