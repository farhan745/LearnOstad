from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Products.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    
]+static (settings.MEDIA_URLS,document_root=settings.MEDIA_ROOT)
