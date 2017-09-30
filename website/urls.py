from django.conf.urls import include,url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documnet_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)