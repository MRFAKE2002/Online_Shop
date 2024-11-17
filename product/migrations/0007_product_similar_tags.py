# Generated by Django 5.0.1 on 2024-02-21 06:57

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_image'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='similar_tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]