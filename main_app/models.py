from django.db import models
from django.urls import reverse


class Fact(models.Model):
    fact = models.TextField(max_length=500)

    def __str__(self):
        return self.fact

    def get_absolut_url(self):
        return reverse('facts_detail', kwargs={'pk': self.id})

class Verbiage(models.Model):
    word = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    definition = models.TextField(max_length=250)
    facts = models.ManyToManyField(Fact)

    def __str__(self):
        return f"{self.word} ({self.language}): {self.definition}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'verbiage_id': self.id})

class Etymology(models.Model):
    year = models.IntegerField()
    example = models.TextField(max_length=250)
    verbiage = models.ForeignKey(Verbiage, on_delete=models.CASCADE)

    def __str__(self):
        return f"Example sentence: {self.example} (appeared on {self.year})."

    class Meta:
        ordering = ['-year']