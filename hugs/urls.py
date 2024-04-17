from django.urls import path
from hugs import views

urlpatterns = [
    path('hugs/', views.HugList.as_view()),
    path('hugs/<int:pk>', views.HugDetail.as_view()),
]
