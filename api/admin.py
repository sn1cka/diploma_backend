from django.contrib import admin
from django.db import models

# Register your models here.
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from api.models import TourPhoto, Tour, TourVariant, Company, CompanyFeed, CompanyContacts, TourDetails


class AdminImageWidget(AdminFileWidget):
	def render(self, name, value, attrs=None, renderer=None):
		output = []
		if value and getattr(value, "url", None):
			image_url = value.url
			file_name = str(value)
			output.append(
				u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s ' % \
				(image_url, image_url, file_name, _('')))
		output.append(super(AdminFileWidget, self).render(name, value, attrs))
		return mark_safe(u''.join(output))


class TourPhotoInline(admin.TabularInline):
	model = TourPhoto
	extra = 1
	fields = ('id', 'tour', 'photo')
	formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}


class CompanyContactsInline(admin.StackedInline):
	model = CompanyContacts


class TourAdmin(admin.ModelAdmin):
	search_fields = ["name"]
	inlines = [TourPhotoInline]
	list_display = (
		"id",
		"name",
		"region",
		"photo",
	)
	formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}


class TourVariantAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"tour",
		"company",
		"coast",
		"date",
	)


class TourDetailsAdmin(admin.ModelAdmin):
	list_display = (
		"difficulty",
		"out_time",
		"back_time",
		"needed_items",
	)


class CompanyAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"name",
	)


class CompanyContactsAdmin(admin.ModelAdmin):
	list_display = (
		"instagram",
		"telegram",
		"whatsapp",
		"phone",
	)


class CompanyFeedAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"name",
	)


admin.site.register(Tour, TourAdmin)
admin.site.register(TourVariant, TourVariantAdmin)
admin.site.register(TourDetails, TourDetailsAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyFeed, CompanyFeedAdmin)
admin.site.register(CompanyContacts, CompanyContactsAdmin)
