# Generated by Django 3.0.5 on 2021-05-29 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_auto_20210529_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='start',
            new_name='star',
        ),
    ]
