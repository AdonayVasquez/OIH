# Generated by Django 2.1.4 on 2019-01-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190125_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivos',
            name='archivo2',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
