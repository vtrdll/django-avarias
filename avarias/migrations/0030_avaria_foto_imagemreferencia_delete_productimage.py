# Generated by Django 5.1.2 on 2025-03-26 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avarias', '0029_remove_avaria_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaria',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='avarias/'),
        ),
        migrations.CreateModel(
            name='ImagemReferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagens_avarias/')),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('avaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='avarias.avaria')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
