from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",views.home),
    path("insta/",include("img_upload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)