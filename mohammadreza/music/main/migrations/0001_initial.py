# Generated by Django 4.2.10 on 2024-02-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cover', models.ImageField(upload_to='covers')),
                ('url', models.URLField()),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
