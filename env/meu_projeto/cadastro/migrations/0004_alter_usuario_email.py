# Generated by Django 5.1.3 on 2024-11-29 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_remove_usuario_aluno_remove_usuario_instituicao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
