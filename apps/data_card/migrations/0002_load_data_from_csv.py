
import csv
import os

from django.db import migrations

def load_initial_data(apps, schema_editor):
    Card = apps.get_model('data_card', 'Card')
    Kind = apps.get_model('data_card', 'Kind')
    Generation = apps.get_model('data_card', 'Generation')
    Element = apps.get_model('data_card', 'Element')
    OriginalDeck = apps.get_model('data_card', 'OriginalDeck')
    app_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(app_dir, 'k-data.csv.data')

    with open(data_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            kind, _ = Kind.objects.get_or_create(name=row[11])
            generation, _ = Generation.objects.get_or_create(name=row[12])
            element, _ = Element.objects.get_or_create(name=row[7])
            original_deck, _ = OriginalDeck.objects.get_or_create(
                name=row[13]
            )

            attack = None if row[8] == "" or row[8] == "Null" else row[8]
            rest = None if row[9] == "" or row[9] == "Null" else row[9]

            Card.objects.create(
                id_k=row[0],
                name=row[1],
                passive=row[2],
                quick_passive=row[3],
                active=row[4],
                quick_active=row[5],
                cost=row[6],
                attack=attack,
                rest=rest,
                description=row[10],
                kind=kind,
                generation=generation,
                element=element,
                original_deck=original_deck,
                rarity=None,
            )


class Migration(migrations.Migration):

    dependencies = [
        ('data_card', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
