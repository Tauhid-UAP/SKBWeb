# Generated by Django 3.0.1 on 2020-01-02 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='pub_date',
        ),
    ]