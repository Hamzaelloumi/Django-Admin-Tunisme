# Generated by Django 2.1 on 2019-03-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190312_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hote',
            fields=[
                ('id_hote', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('Image', models.ImageField(default='default.jpg', upload_to='hotes')),
            ],
        ),
    ]
