# Generated by Django 4.1 on 2022-08-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
