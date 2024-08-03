from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    posts = Post.objects.filter(is_published=True, category__is_published=True).order_by('pub_date')
    context = {'post_list': posts[::-1]}
    return render(request, 'blog/index.html', context)


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug, is_published=True)
    posts = category.post_set.filter(is_published=True,)
    context = {'category': category, 'posts': posts}
    return render(request, 'blog/category.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, is_published=True, category__is_published=True)
    return render(request, 'blog/detail.html', {'post': post})
