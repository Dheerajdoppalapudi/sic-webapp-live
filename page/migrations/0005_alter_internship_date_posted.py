# Generated by Django 4.0 on 2022-02-10 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_internship_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
