from django.urls import path
from . import views

app_name = 'instagram'  # URL Reverse에서 namespace역할을 하게 된다.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail),
    path('archives/<int:year>/', views.archives_year),
]
