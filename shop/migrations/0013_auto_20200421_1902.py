# Generated by Django 3.0.4 on 2020-04-21 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20200421_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='item',
            new_name='name',
        ),
    ]
