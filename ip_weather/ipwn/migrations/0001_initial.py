# Generated by Django 2.0.13 on 2019-05-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=39)),
                ('lat', models.CharField(max_length=20)),
                ('long', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=45)),
                ('state_prov', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('country_code', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'IP Address',
                'verbose_name_plural': 'IP Addresses',
            },
        ),
    ]