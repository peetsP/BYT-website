# Generated by Django 3.0.5 on 2020-04-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_img', models.ImageField(upload_to='services_pics')),
                ('service_name', models.TextField()),
                ('service_description', models.TextField()),
            ],
        ),
    ]
