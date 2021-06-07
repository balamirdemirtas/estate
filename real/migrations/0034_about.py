# Generated by Django 3.0.5 on 2021-05-22 16:02

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0033_auto_20210522_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(db_index=True, default='İnformation', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('info', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]