from django.urls import path
from . import views # 현재 디렉토리(blog)의 views.py를 import 합니다.

urlpatterns = [
    path('', views.post_list, name='post_list'),
]