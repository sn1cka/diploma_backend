from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from api.models import TourDetails, TourVariant, Company, CompanyContacts, Tour


class ImageUrlField(serializers.RelatedField):
	def to_representation(self, instance):
		url = instance.photo.url
		request = self.context.get('request', None)
		if request is not None:
			return request.build_absolute_uri(url)

		return url


class TourDetailsSerializer(ModelSerializer):
	out_time = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
	back_time = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)

	class Meta:
		model = TourDetails
		fields = [
			"id",
			"difficulty",
			"out_time",
			"back_time",
			"needed_items",
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


class TourVariantInlineSerializer(ModelSerializer):
	company = CompanySerializer()
	date = serializers.DateField(format="%d.%m.%Y", read_only=True)
	details = TourDetailsSerializer()

	class Meta:
		model = TourVariant
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


class TourVariantSerializer(ModelSerializer):
	tour = TourSerializer()
	company = CompanySerializer()
	date = serializers.DateField(format="%d.%m.%Y", read_only=True)
	details = TourDetailsSerializer()

	class Meta:
		model = TourVariant
		fields = [
			"tour",
			"company",
			"coast",
			"details",
			"date",
		]
