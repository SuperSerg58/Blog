from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),  # Ссылка на главную страницу
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),  # Ссылка на конкретный пост
    path('tags/', tags_list, name='tags_list_url'),  # Ссылка на список тегов
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),  # Ссылка на форму создания тегов
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),  # Ссылка на посты по конкретному тегу
    path('post/new/', post_new, name='post_new'),  # Ссылка на новый пост
    path('post/<str:slug>/edit/', post_edit, name='post_edit_url'),  # Ссылка на изменение поста
]
