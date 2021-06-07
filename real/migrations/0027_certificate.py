# Generated by Django 3.0.5 on 2021-05-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0026_agent_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('name', models.CharField(db_index=True, default='Marka İsmi Giriniz', max_length=200, verbose_name='İsim')),
            ],
        ),
    ]
