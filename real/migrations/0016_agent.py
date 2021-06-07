# Generated by Django 3.0.5 on 2021-05-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0015_auto_20210514_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]