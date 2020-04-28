from django.urls import path  # urlpatterns에 path를 쓰려고 import한 것
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 여기서 name은 이 path의 이름을 의미함
]
