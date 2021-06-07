# Generated by Django 3.0.5 on 2021-05-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='adaNo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='elektrik',
        ),
        migrations.RemoveField(
            model_name='product',
            name='emsal',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gabari',
        ),
        migrations.RemoveField(
            model_name='product',
            name='imar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='m2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='paftaNo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parselNo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='su',
        ),
        migrations.AddField(
            model_name='product',
            name='binaYas',
            field=models.CharField(db_index=True, default='Bina Yaşı', max_length=200, verbose_name='Bina Yaşı'),
        ),
        migrations.AddField(
            model_name='product',
            name='closem2',
            field=models.CharField(db_index=True, default='Kapalı M2', max_length=200, verbose_name='Kapalı M2'),
        ),
        migrations.AddField(
            model_name='product',
            name='kat',
            field=models.CharField(db_index=True, default='Kat Sayısı', max_length=200, verbose_name='Kat Sayısı'),
        ),
        migrations.AddField(
            model_name='product',
            name='kredi',
            field=models.CharField(db_index=True, default='Kredi Uygunluk', max_length=200, verbose_name='Kredi'),
        ),
        migrations.AddField(
            model_name='product',
            name='oda',
            field=models.CharField(db_index=True, default='Oda Sayısı', max_length=200, verbose_name='Oda Sayısı'),
        ),
        migrations.AddField(
            model_name='product',
            name='openm2',
            field=models.CharField(db_index=True, default='Açık M2', max_length=200, verbose_name='Açık Me2'),
        ),
        migrations.AddField(
            model_name='product',
            name='start',
            field=models.CharField(db_index=True, default='Yıldız Sayısı', max_length=200, verbose_name='Yılsız Sayısı'),
        ),
        migrations.AddField(
            model_name='product',
            name='yatak',
            field=models.CharField(db_index=True, default='Yatak Sayısı', max_length=200, verbose_name='Yatak Sayısı'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(db_index=True, default='Fiyatı', max_length=200, verbose_name='Fiyat'),
        ),
    ]
