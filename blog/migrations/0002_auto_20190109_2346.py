# Generated by Django 2.1.4 on 2019-01-10 05:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
