# Generated by Django 4.2.7 on 2023-11-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0003_alter_usuario_cpf_alter_usuario_idade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='UF',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='bairro',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cep',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cidade',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='complemento',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='numero',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rg',
            field=models.CharField(max_length=9, null=True, unique=True),
        ),
    ]
