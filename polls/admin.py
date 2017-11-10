# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
# Register your models here.
