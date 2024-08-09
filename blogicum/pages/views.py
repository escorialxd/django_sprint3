from django.shortcuts import render


def about(request):
    """Страница 'О нас'"""
    return render(request, 'pages/about.html')


def rules(request):
    """Страница с правилами."""
    return render(request, 'pages/rules.html')
