# Generated by Django 3.0.5 on 2021-05-22 12:32

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0030_auto_20210522_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=21),
            preserve_default=False,
        ),
    ]
