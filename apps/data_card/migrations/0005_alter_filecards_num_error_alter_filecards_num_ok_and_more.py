# Generated by Django 5.1.1 on 2024-09-30 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_card', '0004_alter_card_rarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filecards',
            name='num_error',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='filecards',
            name='num_ok',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='filecards',
            name='num_registers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]