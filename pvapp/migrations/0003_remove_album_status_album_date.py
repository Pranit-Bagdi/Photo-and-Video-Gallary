# Generated by Django 4.2 on 2023-04-29 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pvapp', '0002_photosvideo_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='status',
        ),
        migrations.AddField(
            model_name='album',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
