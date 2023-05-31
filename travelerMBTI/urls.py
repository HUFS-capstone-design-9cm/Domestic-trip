from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('form/', views.form),
    path('result/<int:traveler_id>/', views.result),
    path('results/<int:traveler_id>/', views.results),
    path('submit/', views.submit),
    path('search/', views.search),
    path('types/', views.types),
    path('survey/', views.survey),
]
