# Generated by Django 2.1 on 2019-03-08 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_clinique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinique',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]