# Generated by Django 4.0.1 on 2022-01-13 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryId', models.AutoField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ThreeDModel',
            fields=[
                ('ThreeDId', models.AutoField(primary_key=True, serialize=False)),
                ('ModelName', models.CharField(max_length=100)),
                ('ThreeDModelFileName', models.CharField(max_length=100)),
                ('Category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
    ]
