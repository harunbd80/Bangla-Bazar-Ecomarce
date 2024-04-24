# Generated by Django 5.0.3 on 2024-03-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('item', models.CharField(choices=[('vegetables', 'vegetable'), ('fruits', 'fruits'), ('bread', 'bread'), ('meat', 'meat')], max_length=50)),
                ('img', models.ImageField(upload_to='imges')),
                ('price', models.FloatField()),
                ('discription', models.TextField()),
            ],
        ),
    ]