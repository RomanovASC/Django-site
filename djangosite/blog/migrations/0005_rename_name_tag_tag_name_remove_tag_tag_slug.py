# Generated by Django 4.2.6 on 2023-12-17 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag_tag_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='tag_name',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_slug',
        ),
    ]
