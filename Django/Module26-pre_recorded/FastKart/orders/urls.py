from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Products.urls')),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
]+static (settings.MEDIA_URLS,document_root=settings.MEDIA_ROOT)
