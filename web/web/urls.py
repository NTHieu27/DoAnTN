from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('member/', include('django.contrib.auth.urls')),
    path('menber/', include('member.urls')),
    path('profiles/', include('profiles.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
