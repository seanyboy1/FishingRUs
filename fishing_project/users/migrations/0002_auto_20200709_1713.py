# Generated by Django 3.0.6 on 2020-07-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lure',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
