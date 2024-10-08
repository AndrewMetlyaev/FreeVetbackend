# Generated by Django 5.1.1 on 2024-10-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('pet_art', models.CharField(max_length=100)),
                ('pet_weight', models.CharField(max_length=100)),
                ('pet_gender', models.CharField(max_length=50)),
                ('is_homeless', models.BooleanField()),
                ('files', models.FileField(blank=True, null=True, upload_to='questions_files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
