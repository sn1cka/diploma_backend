# Create your views here.
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.models import TourVariant, Tour, Company, CompanyFeed
from api.serializers import TourVariantSerializer, TourSerializer, CompanySerializer, CompanyFeedSerializer, TourVariantCreateSerializer, \
	CompanyFeedCreateSerializer


class TourVariantsViewSet(ModelViewSet):
	queryset = TourVariant.objects.filter(is_active=True)

	serializer_class = TourVariantSerializer
	authentication_classes = []
	permission_classes = [AllowAny]
	http_method_names = ('get', 'post', 'head', 'options')
	pagination_class = None

	filterset_fields = ['tour', ]

	def get_serializer_class(self):
		if self.action == 'create' or self.action == 'update':
			return TourVariantCreateSerializer
		return TourVariantSerializer


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


class CompanyFeedViewSet(APIView):
	queryset = CompanyFeed.objects.all()
	serializer_class = CompanyFeedCreateSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	def post(self, request, format=None):
		serializer = CompanyFeedCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
