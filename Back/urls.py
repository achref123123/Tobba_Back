from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

api_urls = [

    url('', include('authentification.urls')),
    url('', include('traitement.urls')),

]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^backend/', include(api_urls)),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
