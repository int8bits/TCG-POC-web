# Generated by Django 5.1.1 on 2024-09-25 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_card', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_deck', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cards', models.ManyToManyField(related_name='decks', to='data_card.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.extendeduser')),
            ],
        ),
    ]
