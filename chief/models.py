from django.db import models


class Desktop(models.Model):
    brand = models.CharField(max_length=90, verbose_name="Бренд")
    model = models.CharField(max_length=90, verbose_name="Модель")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='cars/', verbose_name="Изображение")

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "Главный"
        verbose_name_plural = "Главный"


class Photo(models.Model):
    image = models.ImageField(upload_to='cars/', verbose_name="Фотография")

    def __str__(self):
        return f'{self.image.name}'

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Description(models.Model):
    image = models.ForeignKey('Photo', on_delete=models.CASCADE, verbose_name='Фото')
    bodywork = models.CharField(max_length=90, verbose_name='Кузов')
    engine = models.CharField(max_length=90, verbose_name='Двигатель')
    transmission = models.CharField(max_length=90, verbose_name='Коробка передач')
    rudder = models.CharField(max_length=90, verbose_name='Руль')
    mileage = models.IntegerField(verbose_name='Пробег')
    color = models.CharField(max_length=90, verbose_name='Цвет')
    volume = models.IntegerField(verbose_name='Объем')
    condition = models.CharField(max_length=90, verbose_name='Состояние')
    description = models.CharField(max_length=250, verbose_name='Описание')

    def __str__(self):
        fields = [f"{field.verbose_name}: {getattr(self, field.name)}" for field in self._meta.fields if
                  field.name != "id"]
        return f"{self.__class__.__name__} (__all__): " + ", ".join(fields)

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Описания"


class Characteristic(models.Model):
    character = models.CharField(max_length=90, verbose_name='Характеристика')
    brand = models.CharField(max_length=90, verbose_name='Бренд')
    model = models.CharField(max_length=90, verbose_name='Марка')
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.character} {self.brand} {self.model} {self.year}"

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "характеристики"


class Favorites(models.Model):
    brand = models.CharField(max_length=90, verbose_name="Бренд")
    model = models.CharField(max_length=90, verbose_name="Модель")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='cars/', verbose_name="Изображение")

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AllCars(models.Model):
    brand = models.CharField(max_length=90, verbose_name="Бренд")
    model = models.CharField(max_length=90, verbose_name="Модель")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='cars/', verbose_name="Изображение")

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "Все машины"
        verbose_name_plural = "Все машины"

class Filters(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='filterss')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='filters')
    year = models.IntegerField()

    def __str__(self):
        return f"{self.price} {self.model} {self.year}"

    class Meta:
        verbose_name = "Фильтры"
        verbose_name_plural = "Фильтры"

