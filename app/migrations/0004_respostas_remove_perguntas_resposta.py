# Generated by Django 4.2.1 on 2023-05-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_person_perguntas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='perguntas',
            name='resposta',
        ),
    ]
