from django.com.urls import urlpatterns
from FoodApp import views

from django.cong.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^food$', views.foodApi),
    url(r'^food/([0-9]+)$', views.foodApi),

    url(r'^recipe$', views.foodApi),
    url(r'^recipe/([0-9]+)$', views.foodApi),


    url(r'^Food/SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)