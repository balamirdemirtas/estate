# Generated by Django 3.0.5 on 2021-05-08 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durum', models.CharField(choices=[('kiralık', 'KİRALIK'), ('satılık', 'SATILIK'), ('satıldı', 'SATILDI')], default='satılık', max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, related_name='City', to='real.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, default='Proje İsmi', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='room',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, related_name='City', to='real.Room'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=21, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='position',
            field=models.CharField(choices=[('1+1', '1+1'), ('2+1', '2+1'), ('3+1', '3+1'), ('4+1', '4+1'), ('5+1', '5+1')], default='1+1', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.ManyToManyField(blank=True, default=None, related_name='Available', to='real.Available'),
        ),
    ]