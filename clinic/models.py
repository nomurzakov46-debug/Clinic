from django.db import models



class Direction(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='directions/')
    description = models.TextField(blank=True)


    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        ordering = ['name']

    def __str__(self):
        return self.name


class Doctor(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    direction = models.ForeignKey(Direction,on_delete=models.PROTECT,related_name='doctors')
    photo = models.ImageField(upload_to='doctors/',blank=True)
    experience = models.PositiveIntegerField(blank=True,null=True,verbose_name='Стаж работы')
    description = models.TextField(blank=True)
    show_on_home = models.BooleanField(default=False,verbose_name='Активное виденние дома')


    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        return self.full_name



class Promotion(models.Model):

    COLOR_CHOICES = [
        ('green', 'Зелёный'),
        ('blue', 'Синий'),
        ('red', 'Красный'),
        ('yellow', 'Жёлтый'),
        ('cyan', 'Голубой'),
]

    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='promotions/')
    end_date = models.DateField()
    is_big = models.BooleanField(default=False)
    color = models.CharField(max_length=20,choices=COLOR_CHOICES,default='green')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


    def __str__(self):
        return self.title


class Equipment(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='equipment/')

    class Meta:
        verbose_name = 'Обородовоние'
        verbose_name_plural = 'Обородования'

    def __str__(self):
        return self.name

class EquipmentFeature(models.Model):
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE,related_name='features')
    text = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.text


class Appointment(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    direction = models.ForeignKey(Direction,on_delete=models.SET_NULL,null=True,blank=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Все приемы'
    
    def __str__(self):
            return self.full_name


class CallRequest(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Перезвон'
        verbose_name_plural = 'Перезвоны'

    def __str__(self):
        return self.full_name



