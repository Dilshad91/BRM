# Generated by Django 3.0.8 on 2020-08-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BRMapp', '0002_auto_20200826_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
