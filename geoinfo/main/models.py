from django.db import models


class Cityinfo(models.Model):
    """
    Модель для таблицы базы данных с информацией о городах

    city - Название города
    country - Страна
    population - численность населения т.ч.
    cont - внешний ключ для связи с таблицей Continents
    """

    city = models.CharField(max_length=100, null=False, verbose_name='Город')
    country = models.CharField(max_length=100, null=False, verbose_name='Страна')
    population = models.IntegerField(null=False, verbose_name='Численность населения')
    cont = models.ForeignKey('Continents', on_delete=models.PROTECT, verbose_name="id континента")

    def __str__(self):
        return f'{self.city}'

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'
        ordering = ('cont', 'city')


class Continents(models.Model):
    """
    Модель для таблицы базы данных с информацией о континентах

    cont_name - Название континента
    slug_name - slug-представление континента
    content - текст статьи о континенте
    """

    cont_name = models.CharField(max_length=100, null=False, verbose_name='Континент')
    slug_name = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")

    def __str__(self):
        return f'{self.cont_name}'

    class Meta:
        verbose_name = 'Континенты'
        verbose_name_plural = 'Континенты'
        ordering = ('cont_name', )
