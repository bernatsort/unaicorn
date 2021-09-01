"""titanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
# we have to import our views file.
# . means from the same folder
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # We want this to be our home page, so we want it just doesn't
    # have to put in any slash at the end, we just leave it blank:
    # views.home: which function we want to retrieve for for this area, which is, you know, just blank.

    # name='name_we_want' to link result to home. Give a name to the page we want to go.
    path('', views.home, name='home'),
    # name='name_we_want' to link home to result. Give a name to the page we want to go.
    path('result/', views.result, name='result')
]
