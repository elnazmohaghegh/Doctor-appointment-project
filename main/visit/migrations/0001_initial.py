# Generated by Django 4.1.3 on 2022-11-16 11:18

from django.db import migrations, models
import django.db.models.deletion
import visit.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pateints', '0003_alter_patient_ins_type'),
        ('doctors', '0007_doctortime_day'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitsReserved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=20)),
                ('end_time', models.CharField(max_length=20)),
                ('cost', models.PositiveIntegerField()),
                ('peygiri', models.PositiveIntegerField(default=visit.models.random_code)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved_doctor', to='doctors.doctor')),
                ('ins_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.insurance')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved_patient', to='pateints.patient')),
            ],
        ),
    ]
