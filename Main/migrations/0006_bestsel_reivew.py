# Generated by Django 5.0.3 on 2024-04-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='bestsel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('discription', models.TextField()),
                ('img', models.ImageField(upload_to='imges')),
            ],
        ),
        migrations.CreateModel(
            name='Reivew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
    ]
