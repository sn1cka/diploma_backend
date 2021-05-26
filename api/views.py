from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.models import TourVariant, Tour
from api.serializers import TourVariantSerializer, TourSerializer


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
