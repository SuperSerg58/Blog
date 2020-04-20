from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin


def posts_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/index.html', {'posts': posts})


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
