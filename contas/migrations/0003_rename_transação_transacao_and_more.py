# Generated by Django 4.2.7 on 2023-11-25 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_alter_transação_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='transação',
            new_name='transacao',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='dt_criação',
            new_name='dt_criacao',
        ),
        migrations.RenameField(
            model_name='transacao',
            old_name='descrição',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='transacao',
            old_name='observações',
            new_name='observacoes',
        ),
    ]
