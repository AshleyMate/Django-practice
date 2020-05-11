from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # settings.AUTH_USER_MODEL은 기본 유저 모델
    # 1측에 해당하는 pk가 post_id라는 이름으로 저장된다
    message = models.TextField()
    # blank가 True라는 것은 꼭 사진을 안넣어도 된다는 것
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    # blank=True로 하면 태그는 필수가 아님
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f"Custom Post object ({self.id})"
        # return "Custom Post object ({})".format(self.id)
        return self.message

    def get_absolute_url(self):
        return reverse("instagram:post_detail", args={self.pk})

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, limit_choices_to={'is_public': True})  # limit_choices_to 는 is_public이 True인 것만 고를수 있게 해준다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
