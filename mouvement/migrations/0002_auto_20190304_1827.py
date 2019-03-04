# Generated by Django 2.1.5 on 2019-03-04 17:27

from django.db import migrations, models
import mouvement.models.asset


class Migration(migrations.Migration):

    dependencies = [
        ('mouvement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=10)),
                ('adresse_mac', models.CharField(blank=True, max_length=50, null=True)),
                ('statut', models.CharField(choices=[(mouvement.models.asset.StatutAsset('SA'), 'Sans affectation'), (mouvement.models.asset.StatutAsset('DISP'), 'Disponible pour affectation'), (mouvement.models.asset.StatutAsset('OUT'), 'Sorti du périmètre'), (mouvement.models.asset.StatutAsset('AFF'), 'Affecté'), (mouvement.models.asset.StatutAsset('CONF'), 'Affecté et conforme')], max_length=10)),
                ('conforme', models.BooleanField(default=False)),
                ('systeme', models.CharField(max_length=25)),
                ('premiere_mes', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=10)),
                ('adresse_mac', models.CharField(blank=True, max_length=50, null=True)),
                ('statut', models.CharField(choices=[(mouvement.models.asset.StatutAsset('SA'), 'Sans affectation'), (mouvement.models.asset.StatutAsset('DISP'), 'Disponible pour affectation'), (mouvement.models.asset.StatutAsset('OUT'), 'Sorti du périmètre'), (mouvement.models.asset.StatutAsset('AFF'), 'Affecté'), (mouvement.models.asset.StatutAsset('CONF'), 'Affecté et conforme')], max_length=10)),
                ('conforme', models.BooleanField(default=False)),
                ('systeme', models.CharField(max_length=25)),
                ('premiere_mes', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
            },
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('prenom', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('matricule', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
            },
        ),
        migrations.AlterModelOptions(
            name='mouvement',
            options={'ordering': ('-modified_at', '-created_at')},
        ),
        migrations.RenameField(
            model_name='mouvement',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='mouvement',
            old_name='last_modified',
            new_name='modified_at',
        ),
        migrations.RemoveField(
            model_name='mouvement',
            name='name',
        ),
    ]
