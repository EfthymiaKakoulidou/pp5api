from django.urls import path
from diary import views

urlpatterns = [
    path('diary/', views.DiaryList.as_view()),
    path('diary/<int:pk>/', views.DiaryDetail.as_view())
]