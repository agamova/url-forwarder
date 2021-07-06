# Generated by Django 3.2.5 on 2021-07-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForwarderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('access_code', models.CharField(max_length=100)),
                ('redirect_url', models.URLField()),
            ],
        ),
    ]