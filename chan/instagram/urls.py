from django.urls import path
from . import views

app_name = 'instagram'  # URL Reverse에서 namespace역할을 하게 된다.

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    # path의 name은 get_absolute_url에서 쓰인다.
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('archives/<int:year>/', views.archives_year),
]
