# Generated by Django 2.1.7 on 2019-03-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='ower',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='ower',
            new_name='owner',
        ),
    ]