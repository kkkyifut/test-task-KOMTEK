from django.db import models


class HandBook(models.Model):
    """Модель для справочника."""

    text = models.TextField('Наименование', max_length=200)
    name = models.CharField('Короткое наименование', max_length=100)
    description = models.TextField('Описание')
    version = models.CharField(
        'Версия', unique=True, blank=False, max_length=50
    )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True, db_index=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    """Модель для элементов справочника."""

    handbook = models.ForeignKey(
        HandBook, on_delete=models.CASCADE,
        related_name='items', verbose_name='Справочник'
    )
    code = models.CharField(
        'Код элемента', unique=True, blank=False, max_length=50
    )
    value = models.TextField('Значение элемента', blank=False)

    class Meta:
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'
