# Generated by Django 5.0.1 on 2024-01-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizABL1', '0002_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_joining',
            field=models.DateField(blank=True, null=True),
        ),
    ]
