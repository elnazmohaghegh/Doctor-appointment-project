# Generated by Django 4.1.3 on 2022-11-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_doctortime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctortime',
            name='end_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='doctortime',
            name='start_time',
            field=models.CharField(max_length=20),
        ),
    ]
