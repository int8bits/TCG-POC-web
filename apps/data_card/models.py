import csv

from django.db import models


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(null=True, blank=True)
    delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Kind(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Generation(BaseModel):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Element(BaseModel):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Rarity(BaseModel):
    name = models.CharField(max_length=32, default="normal")

    def __str__(self):
        return self.name


class OriginalDeck(BaseModel):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Card(BaseModel):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=64)
    passive = models.TextField(blank=True)
    active = models.TextField(blank=True)
    quick_passive = models.TextField(blank=True)
    quick_active = models.TextField(blank=True)
    cost = models.TextField(blank=True)
    description = models.TextField(blank=True)
    attack = models.IntegerField(null=True, blank=True)
    rest = models.IntegerField(null=True, blank=True)
    banned = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="uploads/cards/", null=True, blank=True
    )

    # Foreign keys
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)
    element = models.ForeignKey(
        Element, on_delete=models.CASCADE, null=True, blank=True
    )
    original_deck = models.ForeignKey(
        OriginalDeck, on_delete=models.CASCADE, null=True, blank=True
    )
    rarity = models.ForeignKey(
        Rarity, on_delete=models.CASCADE, default=1, null=True, blank=True
    )

    def __str__(self):
        return self.name


class FileCards(BaseModel):
    file = models.FileField(upload_to="uploads/file_cards/")
    num_registers = models.IntegerField(null=True, blank=True)
    num_ok = models.IntegerField(null=True, blank=True)
    num_error = models.IntegerField(null=True, blank=True)
    id_errors = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.process_csv()

    def process_csv(self):
        # Read CSV File
        csv_file = self.file.read().decode("utf-8").splitlines()
        reader = csv.reader(csv_file)
        next(reader)

        num_ok = 0
        num_error = 0
        id_errors = []

        for row in reader:
            try:
                kind, _ = Kind.objects.get_or_create(name=row[11])
                generation, _ = Generation.objects.get_or_create(name=row[12])
                element, _ = Element.objects.get_or_create(name=row[7])
                original_deck, _ = OriginalDeck.objects.get_or_create(
                    name=row[13]
                )

                attack = None if row[8] == "" or row[8] == "Null" else row[8]
                rest = None if row[9] == "" or row[9] == "Null" else row[9]

                Card.objects.create(
                    id=row[0],
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
                num_ok += 1
            except Exception as e:
                num_error += 1
                id_errors.append(row[0])

        self.num_registers = num_ok + num_error
        self.num_ok = num_ok
        self.num_error = num_error
        self.id_errors = ",".join(id_errors)

        super().save(
            update_fields=[
                "num_registers",
                "num_ok",
                "num_error",
                "id_errors",
            ]
        )


class CardProffer(models.Model):
    id_k = models.CharField(max_length=16, default="0")
    name = models.CharField(max_length=64)
    passive = models.TextField(blank=True)
    active = models.TextField(blank=True)
    quick_passive = models.TextField(blank=True)
    quick_active = models.TextField(blank=True)
    cost = models.TextField(blank=True)
    description = models.TextField(blank=True)
    attack = models.IntegerField(null=True)
    rest = models.IntegerField(null=True)
    banned = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="uploads/cards/", null=True, blank=True
    )
    approved = models.BooleanField(default=False)

    # Foreign keys
    kind = models.IntegerField(null=True, blank=True)
    generation = models.IntegerField(null=True, blank=True)
    element = models.IntegerField(null=True, blank=True)
    original_deck = models.IntegerField(null=True, blank=True)
    rarity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)