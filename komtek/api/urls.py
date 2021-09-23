from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import HandBookViewSet, ItemViewSet

app_name = 'api-v1'

router_v1 = SimpleRouter()
router_v1.register(r'handbooks', HandBookViewSet, basename='handbook')
router_v1.register(
    r'handbooks/(?P<handbook_id>\d+)/items', ItemViewSet, basename='item'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
