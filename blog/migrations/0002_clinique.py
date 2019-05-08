# Generated by Django 2.1 on 2019-03-08 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinique',
            fields=[
                ('id_clinique', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=50)),
                ('document', models.FileField(upload_to='cliniques/')),
            ],
        ),
    ]
