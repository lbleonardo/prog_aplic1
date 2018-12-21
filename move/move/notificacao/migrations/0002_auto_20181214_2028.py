# Generated by Django 2.1.4 on 2018-12-14 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notificacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('esferaPublica', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('prazo', models.IntegerField()),
                ('dataAbertura', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Solucionador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.IntegerField()),
                ('problema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao.Problema')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao.Setor')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=120)),
                ('pai', models.CharField(max_length=120)),
                ('mae', models.CharField(max_length=120)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=14)),
                ('nickname', models.CharField(max_length=20)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao.Setor')),
            ],
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='problema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao.Problema'),
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao.Usuario'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='ocorrencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao.Ocorrencia'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao.Usuario'),
        ),
    ]
