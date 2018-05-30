from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    lang_pro = models.CharField(max_length=500)
    position = models.CharField(max_length=20)

    def __str__(self):
        return self.name