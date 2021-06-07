# Generated by Django 3.0.5 on 2021-05-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0028_auto_20210522_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='center',
            field=models.CharField(db_index=True, default='4', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='highway',
            field=models.CharField(db_index=True, default='6', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='hospital',
            field=models.CharField(db_index=True, default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='market',
            field=models.CharField(db_index=True, default='3', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='scholl',
            field=models.CharField(db_index=True, default='2', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='sea',
            field=models.CharField(db_index=True, default='5', max_length=200),
        ),
    ]
