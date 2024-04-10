from django.urls import path
from reach_out_comments import views

urlpatterns = [
    path('reach_out_comments/', views.Reach_out_commentList.as_view()),
    path('reach_out_comments/<int:pk>', views.Reach_out_commentDetail.as_view())
]