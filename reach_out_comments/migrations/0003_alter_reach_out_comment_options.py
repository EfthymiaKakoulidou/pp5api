# Generated by Django 3.2.25 on 2024-04-14 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reach_out_comments', '0002_rename_content_reach_out_comment_reach_out_comment_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reach_out_comment',
            options={'ordering': ['created_at']},
        ),
    ]
