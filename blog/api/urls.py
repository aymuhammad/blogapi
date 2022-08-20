from django.urls import path
from . import views

urlpatterns = [
    path('',views.ViewList.as_view(), name='post_list'),
    path('posts/', views.PostDetails.as_view(), name='details'),
    path('add',views.AddPost.as_view(),name='Add_List'),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]