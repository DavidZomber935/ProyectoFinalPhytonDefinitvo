from django.contrib import admin
from django.urls import path, include
from django.conf import settings    

urlpatterns = [
    path('', include('core.urls')),
    path('shop/', include('shop.urls')),
    path('productDetails/', include('productDetails.urls')),
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
]

#configuracion extendida de las urls para visualizar multimedia
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
