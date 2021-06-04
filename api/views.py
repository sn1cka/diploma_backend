# Create your views here.
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import TourVariant, Tour, Company, CompanyFeed
from api.serializers import TourVariantSerializer, TourSerializer, CompanySerializer, CompanyFeedSerializer


class TourVariantsViewSet(ModelViewSet):
	queryset = TourVariant.objects.all()

	serializer_class = TourVariantSerializer
	authentication_classes = []
	permission_classes = [AllowAny]
	http_method_names = ('get', 'head', 'options')
	pagination_class = None

	filterset_fields = ['tour', ]


class TourViewSet(ModelViewSet):
	queryset = Tour.objects.all()

	serializer_class = TourSerializer
	authentication_classes = []
	permission_classes = [AllowAny]
	http_method_names = ('get', 'head', 'options')
	pagination_class = None


class CompanyViewSet(ModelViewSet):
	queryset = Company.objects.all()

	serializer_class = CompanySerializer
	authentication_classes = []
	permission_classes = [AllowAny]
	http_method_names = ('get', 'head', 'options')
	pagination_class = None

	@action(methods=["get"], detail=True, url_path="feeds", url_name="company_feeds")
	def get_feeds(self, request, pk=None):
		company = self.get_object()
		queryset = CompanyFeed.objects.filter(company=company)
		serializer = CompanyFeedSerializer(queryset, many=True, context={"request": request})
		return Response(serializer.data)
