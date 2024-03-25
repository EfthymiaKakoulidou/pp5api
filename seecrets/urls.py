from django.urls import path
from seecrets import views

urlpatterns = [
    path('seecrets/', views.SeecretList.as_view()),
]