# Generated by Django 2.1 on 2018-10-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pullup', '0005_auto_20181017_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvik',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='media',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='misto',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='telo',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='vybaveni',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100, unique=True),
        ),
    ]
