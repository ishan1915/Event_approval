from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/', include('calendar_app.urls')),
   # path('accounts/', include('django.contrib.auth.urls')),  # This includes login and logout URLs
]
