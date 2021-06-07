# Generated by Django 3.0.5 on 2021-05-30 10:01

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0040_auto_20210530_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='info_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='info_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_en',
            field=models.TextField(default='Ürün Aaçıklama 263 Ten az 263 çok olmuyacak', max_length=263, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_tr',
            field=models.TextField(default='Ürün Aaçıklama 263 Ten az 263 çok olmuyacak', max_length=263, null=True),
        ),
    ]
