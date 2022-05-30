"""EduTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import TemplateView
import edutech_app.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_main),
    path('courses/', views.show_courses, name='courses'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.Register.as_view(), name='register'),
    path('stream/', views.show_stream),
    path('profile/', views.show_profile),
    path('main/', views.show_main, name='home'),
    path('course/<int:course_id>/', views.show_course, name='course'),

]
