from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('member.urls')),
    path('', include('profiles.urls')),
    path('', include('pay.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
