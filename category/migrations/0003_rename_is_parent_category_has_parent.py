# Generated by Django 5.0.1 on 2024-02-18 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_is_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='is_parent',
            new_name='has_parent',
        ),
    ]
