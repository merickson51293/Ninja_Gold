from django.urls import path

from . import views

urlpatterns = [
    path("", views.ninja_gold),
    path('reset', views.reset),
    path('process_gold', views.process)
]