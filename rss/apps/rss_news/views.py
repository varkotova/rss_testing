from django.shortcuts import render
from apps.rss_news.models import Post
from django.http import HttpResponse, HttpResponseRedirect


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
        return render(request, 'post.html', context)
    except Post.DoesNotExist:
        return HttpResponse('NB')




def sign(request):
    return render(request, 'sign.html')

def signup_user(request):
    if request.POST:
        user_name = request.POST['user_name']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        email = request.POST['email']

        print(user_name)
        print(password)
        print(repeat_password)
        print(email)

        return HttpResponseRedirect('/')
    else:
        return HttpResponse('NB')

def check_user_name(request):
    if request.GET:
        user_name = request.GET['user_name']
        names = {'Katya', 'Anna', 'Dima'}


        if user_name in names:
            return HttpResponse('no',  content_type='text/html')
        else:
            return HttpResponse('ok', content_type='text/html')

    else:
        return HttpResponse('no', content_type='text/html')








