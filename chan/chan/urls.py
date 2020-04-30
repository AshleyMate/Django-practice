from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('instagram/', include('instagram.urls')),
]

# 장고는 실제 서비스시에, media나 static파일 serving을 장고 기본으로 하는 것을 권장하지 않음.
# if settings.DEBUG:가 없더라도 DEBUG가 False면 빈 문자열을 반환하지만, 명시적으로 하기 위해서 쓴다.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
