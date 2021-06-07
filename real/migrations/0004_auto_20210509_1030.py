# Generated by Django 3.0.5 on 2021-05-09 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0003_auto_20210509_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['-id'],
                'unique_together': {('slug', 'name')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Boats', to='real.Category'),
            preserve_default=False,
        ),
    ]