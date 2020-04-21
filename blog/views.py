from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q


def posts_list(request):
    # Подключение формы поиска:
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query))
    else:
        posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

    # создаётся погинация для постов
    paginator = Paginator(posts, 3)  # количество объектов постов на странице
    page_number = request.GET.get('page', 1)  # формирование ссылки /?page=1 по умолчанию 1
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()  # формирование пере-ной для if, чтобы спрятать пагинацию, там где нет

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'blog/index.html', context)


class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', {'post': post})


class PostCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        # отрисовываем форму на странице HTML
        form = PostForm()
        return render(request, 'blog/post_create_form.html', {'form': form})

    def post(self, request):
        # Передаём в форму данные
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)  # Если тег создаётся, переходим на страницу этого тега

        return render(request, 'blog/post_create_form.html', {'form': bound_form})


class PostUpdate(LoginRequiredMixin, View):
    raise_exception = True

    # получение формы
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)  # выбираем слаг, который хотим отредактировать
        bound_form = PostForm(instance=post)  # передаём его в связанную форму
        return render(request, 'blog/post_update_form.html', {'form': bound_form, 'post': post})

    # отправка формы
    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)  # выбираем слаг, который хотим отредактировать
        bound_form = PostForm(request.POST, instance=post)  # передаём его в связанную форму

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)

        return render(request, 'blog/post_update_form.html', {'form': bound_form, 'post': post})


class PostDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_delete_form.html', {'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('posts_list_url'))


# --------------------------------------Tags------------------------------------------------------------
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})


class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', {'tag': tag})


# Вьюха для создание тегов через форму
class TagCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        # отрисовываем форму на странице HTML
        form = TagForm()
        return render(request, 'blog/tag_create.html', {'form': form})

    def post(self, request):
        # Передаём в форму данные
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)  # Если тег создаётся, переходим на страницу этого тега

        return render(request, 'blog/tag_create.html', {'form': bound_form})


# Форма для редактирования Тегов
class TagUpdate(LoginRequiredMixin, View):
    raise_exception = True

    # получение формы
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)  # выбираем слаг, который хотим отредактировать
        bound_form = TagForm(instance=tag)  # передаём его в связанную форму
        return render(request, 'blog/tag_update_form.html', {'form': bound_form, 'tag': tag})

    # отправка формы
    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)  # выбираем слаг, который хотим отредактировать
        bound_form = TagForm(request.POST, instance=tag)  # передаём его в связанную форму

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)

        return render(request, 'blog/tag_update_form.html', {'form': bound_form, 'tag': tag})


class TagDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'blog/tag_delete_form.html', {'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tags_list_url'))
# --------------------------------------Tags------------------------------------------------------------
