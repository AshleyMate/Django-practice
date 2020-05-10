from django.views.generic import ListView, DetailView
from django. http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()

# @login_required
# def post_list(request):
#     # q라는 인자가 있으면 가져오고, 없으면 빈 문자열을 반환해라. 그것을 q에 저장
#     qs = Post.objects.all()
#     # GET인자, 쿼리스트링 인자라고도 하며 url창에 http://127.0.0.1:8000/instagram/?q=내용 이런식으로 쓴다
#     q = request.GET.get('q', '')
#     if q:
#         # filter함수는 특정 조건으로 걸러서 걸러진 요소들로 iterator객체를 만들어서 리턴
#         # message에서 q라는 문자열이 포함된 자료를 찾아서 qs에 저장
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # @@@@앞의 pk는 필드를 지정한 것이고 뒤의 pk는 값을 넘긴것 만약에 post_detail(request, ab)였다면 pk=ab가 된다.@@@@
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#     })

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset = Post.objects.filter(is_public=True))

class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


post_detail = PostDetailView.as_view()


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
