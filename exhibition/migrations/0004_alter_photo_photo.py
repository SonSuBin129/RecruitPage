# Generated by Django 4.1 on 2023-11-03 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.TextField(),
        ),
    ]
