# Generated by Django 4.2 on 2023-04-30 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pvapp', '0007_rename_photosvideo_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='alt_text',
            new_name='lable',
        ),
    ]