from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from work_inno import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('work/', include('apps.job.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
