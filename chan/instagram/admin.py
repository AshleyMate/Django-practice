from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message',
                    'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:72px;"/>')
            # mark_safe를 쓰지 않으면 이미지를 보여주지 않음. 장고의 보안 기능임 따라서
            # mark_safe로 안전하다는 것을 알리는 것

    def message_length(self, post):
        return f"{len(post.message)} 글자"
