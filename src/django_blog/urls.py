"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# 初始化 Django
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

from blog import views

from django.contrib.staticfiles.views import serve
from django.urls import re_path

def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    # path('', views.index, name='index'),
    path('', RedirectView.as_view(url='blog')),  # 根目录时跳转到blog
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),  # 添加这行
]

handler404 = views.page_not_found_error
handler500 = views.page_error
