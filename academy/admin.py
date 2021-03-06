from django.contrib import admin
from .models import Planet, Jedi, Сandidate, Question, Choice, Answer, Grade


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

    list_display_links = (
        'title',
    )


@admin.register(Jedi)
class JediAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'planet',
        'grade',
    )

    list_display_links = (
        'name',
    )

    exclude = ('padavans',)


@admin.register(Сandidate)
class СandidateAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "habitat_planet",
        "email",
    )

    list_display_links = (
        'name',
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )    
   

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "max_count_padavans",
    )   
    
