from django.contrib import admin
from django.urls import path, include
from .swagger import urlpatterns as docurlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/post/', include('blog.urls')),
    path('api/v1/user/', include('agro_user.urls')),

]


urlpatterns += docurlpatterns