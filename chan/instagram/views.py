from django.shortcuts import render
from .models import Post


def post_list(request):
    # q라는 인자가 있으면 가져오고, 없으면 빈 문자열을 반환해라. 그것을 q에 저장
    qs = Post.objects.all()
    # GET인자, 쿼리스트링 인자라고도 하며 url창에 http://127.0.0.1:8000/instagram/?q=내용 이런식으로 쓴다
    q = request.GET.get('q', '')
    if q:
        # filter함수는 특정 조건으로 걸러서 걸러진 요소들로 iterator객체를 만들어서 리턴
        # message에서 q라는 문자열이 포함된 자료를 찾아서 qs에 저장
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })
