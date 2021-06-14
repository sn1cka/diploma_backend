from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from api.models import TourVariantDetail, TourVariant, Company, CompanyContacts, Tour, CompanyFeed


class FilterActiveTourVariantsSerializer(serializers.ListSerializer):
	def to_representation(self, data):
		data = data.filter(is_active=False)
		return super(FilterActiveTourVariantsSerializer, self).to_representation(data)


class ImageUrlField(serializers.RelatedField):
	def to_representation(self, instance):
		url = instance.photo.url
		request = self.context.get('request', None)
		if request is not None:
			return request.build_absolute_uri(url)

		return url


class TourVariantDetailSerializer(ModelSerializer):
	class Meta:
		model = TourVariantDetail
		fields = [
			"title",
			"description",
		]


class CompanyContactsSerializer(ModelSerializer):
	class Meta:
		model = CompanyContacts
		fields = [
			"id",
			"instagram",
			"telegram",
			"whatsapp",
			"phone",
		]


class CompanySerializer(ModelSerializer):
	contacts = CompanyContactsSerializer()

	class Meta:
		model = Company
		fields = [
			"id",
			"name",
			"contacts"
		]


class CompanyFeedSerializer(ModelSerializer):
	photo = serializers.SerializerMethodField()

	class Meta:
		model = CompanyFeed
		fields = [
			"id",
			"company",
			"photo",
			"feed"
		]

	def get_photo(self, feed):
		request = self.context.get('request', None)
		photo_url = feed.photo.url
		if request is not None:
			return request.build_absolute_uri(photo_url)
		return photo_url


class TourVariantInlineSerializer(ModelSerializer):
	company = CompanySerializer()
	date = serializers.DateField(format="%d.%m.%Y", read_only=True)
	details = TourVariantDetailSerializer(many=True)

	class Meta:
		model = TourVariant
		list_serializer_class = FilterActiveTourVariantsSerializer

		fields = [
			"company",
			"coast",
			"details",
			"date",
		]


class TourSerializer(ModelSerializer):
	photos = ImageUrlField(
		many=True,
		read_only=True,
	)
	variants = TourVariantInlineSerializer(many=True)

	class Meta:
		model = Tour
		fields = [
			"id",
			"photo",
			"name",
			"region",
			"photos",
			"variants",
		]


class TourVariantCreateSerializer(ModelSerializer):
	out_time = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
	back_time = serializers.DateTimeField(format="%d.%m.%Y %H:%M")

	date = serializers.DateField(format="%d.%m.%Y", read_only=True)
	details = TourVariantDetailSerializer(many=True)

	def create(self, validated_data):
		details = validated_data.pop('details')
		tour_variant = TourVariant.objects.create(**validated_data)

		for detail in details:
			detail = TourVariantDetail.objects.create(tour=tour_variant, title=detail['title'], description=detail["description"])
			tour_variant.details.add(detail)
		return tour_variant

	class Meta:
		model = TourVariant
		fields = [
			"id",
			"tour",
			"company",
			"coast",
			"details",
			"date",
			"out_time",
			"back_time",
			"difficulty",
			"photographer",
		]


class TourVariantSerializer(ModelSerializer):
	out_time = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
	back_time = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)

	company = CompanySerializer()
	date = serializers.DateField(format="%d.%m.%Y", read_only=True)
	details = TourVariantDetailSerializer(many=True)

	class Meta:
		model = TourVariant
		fields = [
			"id",
			"tour",
			"company",
			"coast",
			"details",
			"date",
			"out_time",
			"back_time",
			"difficulty",
			"photographer",
		]
