"""
URL configuration for NewPrj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home import views
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Apil Ice Cream Shop Admin"
admin.site.site_title = "Apil Ice Cream Shop Portal"
admin.site.index_title = "Welcome to Apil Ice Cream Shop Portal"

urlpatterns = [
    path("", views.index, name = "home"),
    path("about/", views.about, name = "about"),
    path("contact/", views.contact, name = "contact"),
    path("services/", views.services, name = "services"),
    
]
