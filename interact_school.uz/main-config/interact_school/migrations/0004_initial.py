# Generated by Django 4.1.6 on 2024-01-11 15:20

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interact_school', '0003_delete_blog_delete_carusel_remove_content_title_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('about', models.CharField(max_length=140)),
                ('image', models.URLField()),
                ('blog_content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('any_url', models.URLField(blank=True)),
                ('image', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Langulages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interact_school.category')),
            ],
        ),
        migrations.CreateModel(
            name='MainTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('language_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interact_school.langulages')),
            ],
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('maintitle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interact_school.maintitles')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content_text', ckeditor.fields.RichTextField()),
                ('title_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interact_school.titles')),
            ],
        ),
    ]
