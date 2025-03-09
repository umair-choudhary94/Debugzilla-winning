# Generated by Django 5.1.4 on 2025-03-09 07:20

import datetime
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='A brief description or summary of the blog post', max_length=500)),
                ('publication_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('thumbnail', models.ImageField(blank=True, help_text='Blog thumbnail image', null=True, upload_to='thumbnailbs')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Content')),
                ('author', models.CharField(default='engr umair', max_length=255)),
                ('slug', models.SlugField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-publication_datetime'],
            },
        ),
    ]
