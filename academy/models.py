from django.db import models
from django.urls import reverse
import time


class Planet(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(default='')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Jedi(models.Model):
    GRADE_CHOICES = (
        ('grand-master', 'Grand-Master'),
        ('master', 'Master'),
        ('knight', 'Knight'),
        ('padawan', 'Padawan'),
    )

    name = models.CharField(max_length=250)
    planet = models.ForeignKey(Planet,  on_delete=models.CASCADE)
    grade = models.CharField(max_length=25, choices=GRADE_CHOICES, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jedi_detail", kwargs={"slug": self.id})


class Сandidate(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveSmallIntegerField()
    habitat_planet = models.ForeignKey(Planet,  on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
