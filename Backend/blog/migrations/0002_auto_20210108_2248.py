# Generated by Django 3.1.5 on 2021-01-08 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryfirst',
            new_name='category',
        ),
    ]
