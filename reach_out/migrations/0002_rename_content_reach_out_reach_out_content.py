# Generated by Django 3.2.25 on 2024-03-26 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reach_out', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reach_out',
            old_name='content',
            new_name='reach_out_content',
        ),
    ]
