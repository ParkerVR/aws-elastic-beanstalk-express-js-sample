# Generated by Django 3.1.3 on 2020-11-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plate', models.CharField(max_length=60)),
                ('Latitude', models.CharField(max_length=60)),
                ('Longitude', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
