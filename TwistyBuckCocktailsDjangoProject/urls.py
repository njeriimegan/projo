"""
URL configuration for TwistyBuckCocktailsDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views as myviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myviews.home, name='index-url'),
    path('about/', myviews.about, name='about-url'),
    path('error/', myviews.error, name='error-url'),
    path('blog/', myviews.blog, name='blog-url'),
    path('book/', myviews.book, name='book-url'),
    path('event/', myviews.event, name='event-url'),
    path('menu/', myviews.menu, name='menu-url'),
    path('products/', include('products.urls'))

]
