# Generated by Django 5.1.2 on 2024-11-15 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_card', '0002_load_data_from_csv'),
        ('deck_creator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='cards_not_found',
        ),
        migrations.CreateModel(
            name='CardNotFound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_k', models.CharField(max_length=16, unique=True)),
                ('own_deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck_creator.deck')),
                ('proffer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_card.cardproffer')),
            ],
        ),
    ]
