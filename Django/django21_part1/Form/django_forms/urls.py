
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from main.views import employee_data,home
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('main.urls'))
    path('',home,name="home"),
    path('employee/',employee_data,name="employee"),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
