from django.contrib import admin
from .models import Traveler, Question, Choice, Spot, Survey

admin.site.register(Traveler)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Spot)
admin.site.register(Survey)
