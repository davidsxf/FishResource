# Generated by Django 3.2.2 on 2021-07-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('province', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
                ('area', models.CharField(blank=True, max_length=32, null=True)),
                ('town', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'province',
                'managed': False,
            },
        ),
    ]