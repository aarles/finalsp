# Generated by Django 4.2.1 on 2023-05-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_respostas_remove_perguntas_resposta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Respostas',
        ),
        migrations.AddField(
            model_name='perguntas',
            name='resposta',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
