from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Tag
from .forms import PostForm


def posts_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, slug):
    # post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', {'tag': tag})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)  # Строим форму
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_url', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
