# Generated by Django 3.0.5 on 2021-11-21 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20211121_0548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='availabe',
            new_name='available',
        ),
    ]