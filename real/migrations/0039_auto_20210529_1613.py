# Generated by Django 3.0.5 on 2021-05-29 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0038_auto_20210529_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='City', to='real.Room', verbose_name='Type'),
        ),
    ]