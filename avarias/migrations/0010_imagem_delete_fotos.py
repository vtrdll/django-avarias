# Generated by Django 5.1.2 on 2025-03-19 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avarias', '0009_remove_avaria_photo_fotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='avarias/')),
                ('descrição', models.CharField(blank=True, max_length=255, null=True)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='imagens', to='avarias.avaria')),
            ],
        ),
        migrations.DeleteModel(
            name='Fotos',
        ),
    ]
