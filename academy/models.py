from django.db import models
from django.urls import reverse
import time


class Planet(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(default='')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title.title()


class Grade(models.Model):
    title = models.CharField(max_length=250)
    max_count_padavans = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('title',)
        ordering = ('title',)

    def __str__(self):
        return self.title.title()


class Jedi(models.Model):
    name = models.CharField(max_length=250)
    planet = models.ForeignKey(Planet,  on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING, default=0)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name.upper()

    def get_absolute_url(self):
        return reverse("jedi_detail", kwargs={"slug": self.id})


class Сandidate(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveSmallIntegerField()
    habitat_planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    email = models.EmailField()
    jedi = models.ForeignKey(Jedi, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='sensei')
    answered_questions = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name.upper()

    def get_absolute_url(self):
        return reverse("candidate_detail", kwargs={"slug": self.id})


class Choice(models.Model):
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title.title()


class Question(models.Model):
    title = models.CharField(max_length=4096)
    visible = models.BooleanField(default=False)
    choice = models.ManyToManyField(Choice)

    def __str__(self):
           return self.title.title()

    def get_absolute_url(self):
        return reverse("question", kwargs={"pk": self.id})


class Answer(models.Model):
    candidate = models.ForeignKey(Сandidate, on_delete=models.CASCADE, blank=True, null=True)
    qestions = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    ans = models.ForeignKey(Choice, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.id

