# Generated by Django 4.2.15 on 2024-08-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('startTime', models.DateTimeField(auto_now=True)),
                ('endTime', models.DateTimeField(verbose_name='End')),
            ],
        ),
    ]
