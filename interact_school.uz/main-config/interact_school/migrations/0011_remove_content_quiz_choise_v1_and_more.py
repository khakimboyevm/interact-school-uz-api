# Generated by Django 4.1.6 on 2024-01-23 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interact_school', '0010_content_quiz_choise_v1_2_content_quiz_choise_v2_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='quiz_choise_v1',
        ),
        migrations.RemoveField(
            model_name='content',
            name='quiz_choise_v1_2',
        ),
        migrations.RemoveField(
            model_name='content',
            name='quiz_choise_v2',
        ),
        migrations.RemoveField(
            model_name='content',
            name='quiz_choise_v2_2',
        ),
        migrations.RemoveField(
            model_name='content',
            name='quiz_choise_v3',
        ),
        migrations.RemoveField(
            model_name='content',
            name='quiz_choise_v3_3',
        ),
        migrations.RemoveField(
            model_name='content',
            name='quiz_choise_v4',
        ),
        migrations.RemoveField(
            model_name='content',
            name='quiz_choise_v4_4',
        ),
        migrations.RemoveField(
            model_name='content',
            name='quiz_title',
        ),
        migrations.RemoveField(
            model_name='content',
            name='quiz_title2',
        ),
    ]
