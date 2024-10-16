# Generated by Django 5.1.1 on 2024-10-16 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetbook', '0002_vetbook_chip_install_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(max_length=255)),
                ('visit_date', models.DateField()),
                ('complaints', models.TextField(blank=True, null=True)),
                ('doctor_conclusion', models.TextField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='clinic_visits_files/')),
                ('vetbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_visits', to='vetbook.vetbook')),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedTreatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_name', models.CharField(max_length=255)),
                ('dosage', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('missed_doses', models.CharField(blank=True, max_length=100, null=True)),
                ('calendar', models.TextField(blank=True, null=True)),
                ('vetbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extended_treatments', to='vetbook.vetbook')),
            ],
        ),
    ]