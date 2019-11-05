from django.db import models


class Trainer(models.Model):
    nickname = models.CharField(max_length=20, default='Anonymous')
    img = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname


class Pokemon(models.Model):
    pokemon_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    attack = models.IntegerField(null=False, blank=False)
    defense = models.IntegerField(null=False, blank=False)
    stamina = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
