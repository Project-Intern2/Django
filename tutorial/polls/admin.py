from django.contrib import admin

from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ("Question text", {"fields": ["question_text"]}),
        ("Was published recently", {"fields": ["was_published_recently"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', "was_published_recently")


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
