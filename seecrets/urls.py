from django.urls import path
from seecrets import views

urlpatterns = [
    path('seecrets/', views.SeecretList.as_view()),
    path('seecrets/<int:pk>/', views.SeecretDetail.as_view()),
]