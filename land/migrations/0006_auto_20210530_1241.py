# Generated by Django 3.0.5 on 2021-05-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0005_auto_20210530_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='position',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='room',
            name='position_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='position_tr',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]
