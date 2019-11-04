from django.db import models


class Trainer(models.Model):
    nickname = models.CharField(max_length=20, default='Anonymous')
    img = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
