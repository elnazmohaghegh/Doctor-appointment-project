# Generated by Django 4.1.3 on 2022-11-16 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_remove_doctortime_reserved'),
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitsreserved',
            name='reserved_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserved_date', to='doctors.doctortime'),
        ),
    ]
