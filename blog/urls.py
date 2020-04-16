from django.urls import path
from .views import *

urlpatterns = [
    # Посты
    path('', posts_list, name='posts_list_url'),  # Ссылка на главную страницу
    path('post/create/', PostCreate.as_view(), name='post_create_url'),  # Ссылка на форму создания поста
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),  # Ссылка на конкретный пост
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),  # Ссылка на изменение поста
    # Тэги
    path('tags/', tags_list, name='tags_list_url'),  # Ссылка на список тегов
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),  # Ссылка на форму создания тегов
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),  # Ссылка на посты по конкретному тегу
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),  # Изменение тегов
]
