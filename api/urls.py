import imp
from django.urls import re_path
from api import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^category$' , views.categoryApi),
    re_path(r'^category/([0-9]+)$' , views.categoryApi),

    re_path(r'^model$' , views.threeDModelApi),
    re_path(r'^model/([0-9]+)$' , views.threeDModelApi),

    re_path(r'^model/savemodel' , views.saveModel)

]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)