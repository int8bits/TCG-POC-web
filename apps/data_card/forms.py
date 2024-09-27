
import csv

from django import forms

from .models import Card, Element, FileCards, Generation, Kind, OriginalDeck


class FileCardsForm(forms.ModelForm):
    class Meta:
        model = FileCards
        fields = ['file']

    def save(self):
        errors = []
        object_file = self.cleaned_data["file"].read().decode("utf-8")
        reader = csv.reader(object_file.splitlines())
        next(reader)

        for row in reader:
            try:
                kind, _ = Kind.objects.get_or_create(name=row[11])
                generation, _ = Generation.objects.get_or_create(name=row[12])
                element, _ = Element.objects.get_or_create(name=row[7])
                original_deck, _ = OriginalDeck.objects.get_or_create(
                    name=row[13]
                )
                print(kind, generation, element, original_deck)
                Card.objects.create(
                    id=row[0],
                    name=row[1],
                    passive=row[2],
                    quick_passive=row[3],
                    active=row[4],
                    quick_active=row[5],
                    cost=row[6],
                    attack=row[8],
                    rest=row[9],
                    description=row[10],
                    kind=kind,
                    generation=generation,
                    element=element,
                    original_deck=original_deck,
                    rarity=None,
                )
            except Exception as e:
                print(e)
                errors.append(row[0])

            # break

        print(errors)

        FileCards.objects.create(
            file=self.cleaned_data['file'],
        )