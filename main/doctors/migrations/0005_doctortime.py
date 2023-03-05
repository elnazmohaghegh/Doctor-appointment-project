# Generated by Django 4.1.3 on 2022-11-16 10:36

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_alter_doctor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', django_jalali.db.models.jDateTimeField()),
                ('end_time', django_jalali.db.models.jDateTimeField()),
                ('reserved', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_times', to='doctors.doctor')),
            ],
        ),
    ]