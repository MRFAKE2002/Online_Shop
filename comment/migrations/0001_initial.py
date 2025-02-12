# Generated by Django 5.0.1 on 2024-02-11 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('rate', models.PositiveIntegerField(default=1, verbose_name='rate')),
                ('datetime_create', models.DateTimeField(auto_now_add=True, verbose_name='datetime_create')),
                ('is_reply', models.BooleanField(default=False, verbose_name='is_reply')),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='published', max_length=20, verbose_name='status')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='product.product', verbose_name='product')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_replies', to='comment.comment', verbose_name='reply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
