from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.conf import settings
from .models import Post, Category
from django.http import Http404


def index(request):
    posts = Post.objects.published()[:settings.PAGINATOR]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug, is_published=True)
    post_list = category.posts.published()
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post.objects.published(), id=id)
    if post.pub_date > timezone.now():
        raise Http404('Пост не найден')
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
