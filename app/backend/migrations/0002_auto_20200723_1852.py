# Generated by Django 3.0.7 on 2020-07-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
