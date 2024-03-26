from django.urls import path
from reach_out import views

urlpatterns = [
    path('reach_out/', views.Reach_outList.as_view()),
    path('reach_out/<int:pk>', views.Reach_outDetail.as_view())
]