from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import TourVariantDetail, TourVariant, Company, CompanyContacts, Tour, CompanyFeed


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
    # photo = ImageUrlField(read_only=True)
    photo = serializers.SerializerMethodField()

    class Meta:
        model = CompanyFeed
        fields = [
            "id",
            "name",
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
        fields = [
            "id",
            "tour",
            "company",
            "coast",
            "date",
            "difficulty",
            "out_time",
            "back_time",
            "photographer",
            "start_height",
            "max_height",
            "days_count",
            "path_length_m",
            "needed_items",
            "details",
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
            "needed_items"
        ]
