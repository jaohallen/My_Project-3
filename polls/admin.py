# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# Register your models here.
