# Generated by Django 3.0.5 on 2021-05-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0014_auto_20210514_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manager',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
    ]
