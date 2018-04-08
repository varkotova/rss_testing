from django.shortcuts import render
import random


def index(request):
    context = {

    }
    return render(request, 'index.html', context)



