from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url


handler404 = 'handbooks.views.page_not_found'
handler500 = 'handbooks.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api-v1')),
    path('', include('handbooks.urls', namespace='handbooks')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="HandBooks API",
        default_version='v1',
        description="Документация приложения handbooks проекта test-task-KOMTEK",
        # terms_of_service="URL страницы с пользовательским соглашением",
        contact=openapi.Contact(email="admin@komtek.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
