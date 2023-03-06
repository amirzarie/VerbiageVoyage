from django.db import models
from django.urls import reverse


class Verbiage(models.Model):
    word = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    definition = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.word} ({self.language}): {self.definition}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'verbiage_id': self.id})

class Etymology(models.Model):
    date = models.IntegerField()
    example = models.TextField(max_length=250)
    verbiage = models.ForeignKey(Verbiage, on_delete=models.CASCADE)

    def __str__(self):
        return f"First appeared on {self.date}. Example sentence: {self.example}"