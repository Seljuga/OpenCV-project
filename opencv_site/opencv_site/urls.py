
from django.urls import path
from imageapp.views import upload_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', upload_view, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
