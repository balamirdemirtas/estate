# Generated by Django 3.0.5 on 2021-05-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0009_auto_20210514_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='m2',
            field=models.CharField(db_index=True, default='m2', max_length=200),
        ),
    ]
