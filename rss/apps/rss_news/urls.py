"""rss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from apps.rss_news import views


# До Django 2.0
# urlpatterns = [
#     url('^test/(?P<number>[0-9]*)$', views.test, name='test'),
#     url('^test/$', views.page, name="page")
# ]

# Django 2.0
# urlpatterns = [
#     path('test/<int:testvar>', views.test, name='test'),
#     path('page/', views.page, name="page")
# ]


urlpatterns = [
    path('', views.index),
    path('post/<slug:number_or_letter>/', views.post),

]
