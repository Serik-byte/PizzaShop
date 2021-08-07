from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Категории"

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/%Y/%m/')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукты"

    def __str__(self):
        return f'Продукд {self.name}'


class ContactU(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Контакты от пользователей"

    def __str__(self):
        return f'Сообщение от пользователя {self.name}'


class Chef(models.Model):
    fullname = models.CharField(max_length=25, verbose_name="Имя повора")
    professional_skills = models.CharField(max_length=255, verbose_name="Навыки повора")
    content = models.TextField(verbose_name="Информация о поворе")
    image = models.ImageField(upload_to='images/%Y/%m/', verbose_name="Изображение повора")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата принятии на работу")

    class Meta:
        verbose_name = "Список поворов"

    def __str__(self):
        return f'Информация о поворе {self.name}'