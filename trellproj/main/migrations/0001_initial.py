# Generated by Django 3.0.8 on 2020-10-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('direction', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('startTime', models.TimeField(blank=True)),
                ('endTime', models.TimeField(blank=True)),
                ('ticketPrice', models.PositiveIntegerField(blank=True)),
                ('totalTickets', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]
