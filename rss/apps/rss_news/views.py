from django.shortcuts import render
from apps.rss_news.models import Post
from django.http import HttpResponse


def index(request):

    posts = reversed(Post.objects.all())

    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)

def post(request, number_or_letter):

    try:
        context = {
            'post': Post.objects.get(id=number_or_letter)
        }
    except Post.DoesNotExist:
        return HttpResponse('NB')

    return render(request, 'post.html', context)




