# Generated by Django 4.1.6 on 2024-01-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interact_school', '0008_content_quiz_choise_v1_content_quiz_choise_v2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='quiz_title2',
            field=models.CharField(blank=True, max_length=4096),
        ),
    ]