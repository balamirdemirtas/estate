# Generated by Django 3.0.5 on 2021-05-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='taputype',
            field=models.CharField(db_index=True, default='Tapu Durumu', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='airport',
            field=models.CharField(db_index=True, default='Hava Alanına Uzaklık', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='anayol',
            field=models.CharField(db_index=True, default='Anayola Uzaklık', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='center',
            field=models.CharField(db_index=True, default='Merkeze Uzaklık', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='sea',
            field=models.CharField(db_index=True, default='Denize Uzaklık', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='su',
            field=models.CharField(db_index=True, default='Su', max_length=200),
        ),
    ]