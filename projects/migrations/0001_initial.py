# Generated by Django 2.0.4 on 2018-05-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParserPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=250)),
                ('photos', models.CharField(max_length=50)),
            ],
        ),
    ]
