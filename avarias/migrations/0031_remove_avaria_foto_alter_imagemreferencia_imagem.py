# Generated by Django 5.1.2 on 2025-03-26 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avarias', '0030_avaria_foto_imagemreferencia_delete_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaria',
            name='foto',
        ),
        migrations.AlterField(
            model_name='imagemreferencia',
            name='imagem',
            field=models.ImageField(upload_to='avarias/'),
        ),
    ]
