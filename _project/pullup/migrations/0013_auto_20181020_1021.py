# Generated by Django 2.1 on 2018-10-20 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pullup', '0012_auto_20181020_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='PouzitiMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zaznam_unique', models.CharField(max_length=50)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pullup.Media')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='pouzitimedia',
            unique_together={('media', 'zaznam_unique')},
        ),
    ]
