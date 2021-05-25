# Generated by Django 3.2.3 on 2021-05-25 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='CompanyContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Instagram')),
                ('telegram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telegram')),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True, verbose_name='WhatsApp')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'Контакты компании',
                'verbose_name_plural': 'Контакты компаний',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='tour_images', verbose_name='Фото')),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
                ('region', models.CharField(max_length=1024, verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.CreateModel(
            name='TourDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=255, verbose_name='Сложность')),
                ('out_time', models.DateTimeField(verbose_name='Время выхода')),
                ('back_time', models.DateTimeField(verbose_name='Время возвращения')),
                ('needed_items', models.CharField(max_length=255, verbose_name='Необходимые вещи')),
            ],
            options={
                'verbose_name': 'Детали тура',
                'verbose_name_plural': 'Детали туров',
            },
        ),
        migrations.CreateModel(
            name='TourVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coast', models.PositiveIntegerField(verbose_name='Цена')),
                ('date', models.DateField(verbose_name='Дата')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='api.company', verbose_name='Компания')),
                ('details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='variant', to='api.tourdetails', verbose_name='Детали тура')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='api.tour', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Вариант тура',
                'verbose_name_plural': 'Варианты туров',
            },
        ),
        migrations.CreateModel(
            name='TourPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='tour_images', verbose_name='Фото')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='api.tour')),
            ],
            options={
                'verbose_name': 'Фото тура',
                'verbose_name_plural': 'Фотографии тура',
            },
        ),
        migrations.CreateModel(
            name='CompanyFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='feed_images', verbose_name='Фото')),
                ('feed', models.CharField(max_length=1024, verbose_name='Отзыв')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='api.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Отзыв о компании',
                'verbose_name_plural': 'Отзывы о компании',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='contacts',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='api.companycontacts', verbose_name='Контакты'),
        ),
    ]