from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list_url'),
    path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit_url'),
]
