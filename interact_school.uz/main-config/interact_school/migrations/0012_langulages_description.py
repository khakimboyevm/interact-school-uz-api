# Generated by Django 4.1.6 on 2024-01-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interact_school', '0011_remove_content_quiz_choise_v1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='langulages',
            name='description',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
    ]
