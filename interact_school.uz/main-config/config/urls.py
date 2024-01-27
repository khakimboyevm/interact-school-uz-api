
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("interact_school.urls")),
    path('api/auth/', include('rest_framework.urls')),
    path("", include("ai_chat.urls")),
    path('admin/', admin.site.urls),
]
