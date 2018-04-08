from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return HttpResponse('HI!')

def kokoko(request):

    return HttpResponse('kokoko')

