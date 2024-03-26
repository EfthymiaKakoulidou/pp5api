from django.urls import path
from blog import views

urlpatterns = [
    path('blogposts/', views.BlogList.as_view()),
    path('blogpost/<int:pk>/', views.BlogDetail.as_view())
]