# Generated by Django 5.0.1 on 2024-02-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizABL1', '0009_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='submit_time',
            field=models.DateTimeField(null=True),
        ),
    ]
