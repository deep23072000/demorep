# Generated by Django 4.1.4 on 2023-01-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255)),
                ('heading', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
    ]
