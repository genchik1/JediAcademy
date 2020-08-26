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


class Grade(models.Model):
    title = models.CharField(max_length=250)
    max_count_padavans = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('title',)
        ordering = ('title',)

    def __str__(self):
        return self.title


class Jedi(models.Model):
    # GRADE_CHOICES = (
    #     ('grand-master', 'Grand-Master'),
    #     ('master', 'Master'),
    #     ('knight', 'Knight'),
    #     ('padawan', 'Padawan'),
    # )

    name = models.CharField(max_length=250)
    planet = models.ForeignKey(Planet,  on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING, default=0)
    # grade = models.CharField(max_length=25, choices=GRADE_CHOICES, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jedi_detail", kwargs={"slug": self.id})


class Сandidate(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveSmallIntegerField()
    habitat_planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    email = models.EmailField()
    sensei = models.ForeignKey(Jedi, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("candidate_detail", kwargs={"slug": self.id})



class Choice(models.Model):
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=4096)
    visible = models.BooleanField(default=False)
    choice = models.ManyToManyField(Choice)

    def __str__(self):
           return self.title

    def get_absolute_url(self):
        return reverse("question", kwargs={"pk": self.id})



class Answer(models.Model):
    candidate = models.ForeignKey(Сandidate, on_delete=models.CASCADE)
    qestions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

