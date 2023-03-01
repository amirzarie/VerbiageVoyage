from django.db import models

# Create your models here.
class Verbiage(models.Model):
    word = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    definition = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.word} ({self.language}): {self.definition}"

