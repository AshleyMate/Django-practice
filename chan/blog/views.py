from django.shortcuts import render
from .models import Post


def post_list(request):
    # qs = Queryset -> 전달받은 객체의 목록, 데이터베이스로부터 데이터를 읽고, 필터를 걸거나 정렬할 수 있음
    qs = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })
