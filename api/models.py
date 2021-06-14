from django.db import models


# Create your models here.
from api.choices import tour_difficulties


class Tour(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="tour_images")
    name = models.CharField(max_length=100, verbose_name="Название")
    region = models.CharField(max_length=100, verbose_name="Регион")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class TourPhoto(models.Model):
    tour = models.ForeignKey(Tour, related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="Фото", upload_to="tour_images")

    class Meta:
        verbose_name = "Фото тура"
        verbose_name_plural = "Фотографии тура"


class CompanyContacts(models.Model):
    instagram = models.CharField(max_length=255, verbose_name="Instagram", null=True, blank=True)
    telegram = models.CharField(max_length=255, verbose_name="Telegram", null=True, blank=True)
    whatsapp = models.CharField(max_length=255, verbose_name="WhatsApp", null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name="Phone", null=True, blank=True)

    class Meta:
        verbose_name = "Контакты компании"
        verbose_name_plural = "Контакты компаний"


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    contacts = models.OneToOneField(CompanyContacts, on_delete=models.CASCADE, verbose_name="Контакты",
                                    related_name="company")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class CompanyFeed(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компания", related_name="feeds")

    name = models.CharField(max_length=200, verbose_name="Название")
    photo = models.ImageField(verbose_name="Фото", upload_to="feed_images")
    feed = models.CharField(max_length=1024, verbose_name="Отзыв")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв о компании"
        verbose_name_plural = "Отзывы о компании"


class TourVariant(models.Model):
    tour = models.ForeignKey(Tour, verbose_name="Тур", related_name="variants", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name="Компания", related_name="variants", on_delete=models.CASCADE)
    coast = models.PositiveIntegerField(verbose_name="Цена")

    difficulty = models.CharField(max_length=255, verbose_name="Сложность", choices=tour_difficulties)
    out_time = models.DateTimeField(verbose_name="Время выхода")
    back_time = models.DateTimeField(verbose_name="Время возвращения")
    photographer = models.BooleanField(verbose_name="Наличие фотографа")

    date = models.DateField(verbose_name="Дата")
    start_height = models.PositiveIntegerField(verbose_name="Высота старта")
    max_height = models.PositiveIntegerField(verbose_name="Максимальная высота")
    days_count = models.PositiveIntegerField(verbose_name="Количество дней")
    path_length_m = models.PositiveIntegerField(verbose_name="Длина пешего пути (м)")
    needed_items = models.CharField(max_length=1024, verbose_name="Необходимые вещи")
    is_active = models.BooleanField(verbose_name="Тур активен", default=False)

    def __str__(self):
        return f"{self.tour.name} - {self.company.name}"

    class Meta:
        verbose_name = "Вариант тура"
        verbose_name_plural = "Варианты туров"


class TourVariantDetail(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.CharField(max_length=1024, verbose_name="Описание")
    tour = models.ForeignKey(TourVariant, verbose_name="Тур", on_delete=models.CASCADE, related_name="details")

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = "Деталь тура"
        verbose_name_plural = "Детали туров"
