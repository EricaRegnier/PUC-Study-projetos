from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first.urls')),
    path('verification/', include('verify_email.urls')),
]