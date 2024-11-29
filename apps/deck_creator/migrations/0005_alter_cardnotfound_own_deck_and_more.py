# Generated by Django 5.1.2 on 2024-11-15 01:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_card', '0002_load_data_from_csv'),
        ('deck_creator', '0004_alter_cardnotfound_proffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardnotfound',
            name='own_deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='not_founds', to='deck_creator.deck'),
        ),
        migrations.AlterField(
            model_name='cardnotfound',
            name='proffer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_card.cardproffer'),
        ),
    ]