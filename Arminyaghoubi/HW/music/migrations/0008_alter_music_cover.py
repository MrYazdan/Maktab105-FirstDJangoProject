# Generated by Django 5.0.2 on 2024-02-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_alter_music_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='cover',
            field=models.FileField(upload_to='media/images/'),
        ),
    ]
