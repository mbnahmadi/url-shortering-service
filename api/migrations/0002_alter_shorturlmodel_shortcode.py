# Generated by Django 5.2 on 2025-04-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturlmodel',
            name='shortcode',
            field=models.CharField(blank=True, max_length=8, unique=True, verbose_name='Short Code'),
        ),
    ]
