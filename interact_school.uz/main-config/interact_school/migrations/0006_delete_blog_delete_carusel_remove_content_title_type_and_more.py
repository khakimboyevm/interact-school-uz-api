# Generated by Django 4.1.6 on 2024-01-15 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interact_school', '0005_langulages_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Carusel',
        ),
        migrations.RemoveField(
            model_name='content',
            name='title_type',
        ),
        migrations.RemoveField(
            model_name='langulages',
            name='category_type',
        ),
        migrations.RemoveField(
            model_name='maintitles',
            name='language_type',
        ),
        migrations.RemoveField(
            model_name='titles',
            name='maintitle_type',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='Langulages',
        ),
        migrations.DeleteModel(
            name='MainTitles',
        ),
        migrations.DeleteModel(
            name='Titles',
        ),
    ]
