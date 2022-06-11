from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# add swagger
schema_view = get_schema_view( # new
    openapi.Info(
        title="Technical Task",
        default_version="v1",
        description="Developed by Abdelrahman Ibrahem",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
        public=True,
        permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/users/' , include('users.urls')),
    path('api/lists/' , include('lists.urls')),
    path('api/tasks/' , include('tasks.urls')),
    path('' ,schema_view.with_ui(
    'swagger', cache_timeout=0)
    )
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)