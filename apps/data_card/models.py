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
    passive = models.TextField()
    active = models.TextField()
    quick_passive = models.TextField()
    quick_active = models.TextField()
    cost = models.TextField()
    description = models.TextField()
    attack = models.IntegerField(null=True)
    rest = models.IntegerField(null=True)
    banned = models.BooleanField(default=False)

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
        Rarity, on_delete=models.CASCADE, default=1, null=True
    )

    def __str__(self):
        return self.name


class FileCards(BaseModel):
    file = models.FileField(upload_to="uploads/file_cards/")
    num_registers = models.IntegerField(null=True)
    num_ok = models.IntegerField(null=True)
    num_error = models.IntegerField(null=True)
    id_errors = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file.name