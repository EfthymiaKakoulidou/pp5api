# Generated by Django 3.2.25 on 2024-04-06 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_rename_post_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='seecret',
        ),
    ]
