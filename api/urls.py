from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import TourVariantsViewSet, TourViewSet

schema_view = get_schema_view(
	openapi.Info(
		title="Snippets API",
		default_version='v1',
		description="Test description",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="contact@snippets.local"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
	permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register("tours/variants", TourVariantsViewSet, basename="tour_variants")
router.register("tours", TourViewSet, basename="tours")

urlpatterns = [
	path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('', include('djoser.urls')),
	path('', include('djoser.urls.jwt')),
	path('', include(router.urls)),

]
