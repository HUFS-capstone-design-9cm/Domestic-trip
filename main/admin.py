from django.contrib import admin
from .models import Result, Question, Choice, Spot, Survey

admin.site.register(Result)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Spot)
admin.site.register(Survey)
