from django.db import models
from clinic.models import Direction,Doctor

class OmsRequest(models.Model):

    REGION_CHOICES = [
        ('tomsk','Томская область'),
        ('other','Другой регион')
    ]



    full_name = models.CharField(max_length=100)
    date_birthday = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    profile = models.ForeignKey(Direction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='oms_request')
    service = models.CharField(max_length=200,blank=True)
    region = models.CharField(max_length=20,choices=REGION_CHOICES,default='tomsk')
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    representative = models.CharField(max_length=200, blank=True)
    reason = models.TextField(blank=True)
    source = models.CharField(max_length=200, blank=True)

    document = models.FileField(upload_to='oms/', blank=True)

    class Meta:
        verbose_name = 'Заявка на лечение по ОМС'
        verbose_name_plural = 'Заявки на лечение по ОМС'
    def __str__(self):
        return f'{self.full_name} ({self.phone_number})'


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Ужасно'),
        (2, '2 - Плохо'),
        (3, '3 - Нормально'),
        (4, '4 - Хорошо'),
        (5, '5 - Отлично'),
    ]
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    doctor = models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True,blank=True,related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.doctor} ({self.rating}/5)'


class HistoryEvent(models.Model):
    year = models.PositiveSmallIntegerField()
    text = models.TextField()

    class Meta:
        verbose_name = 'Событие истории'
        verbose_name_plural = 'События истории'
        ordering = ['-year']

    def __str__(self):
        return str(self.year)

    

class ServiceItem(models.Model):
    CATEGORY_CHOICES = [
        ('service', 'Услуга'),
        ('diagnostic', 'Диагностика'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='service',
        verbose_name='Раздел'
    )
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена (сом)')

    class Meta:
        verbose_name = 'Услуга или диагностика'
        verbose_name_plural = 'Услуги и диагностика'

    def __str__(self):
        return f"{self.get_category_display()} — {self.name}"
