# Generated by Django 4.1.3 on 2022-11-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_remove_doctortime_reserved'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='dr_cost',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
