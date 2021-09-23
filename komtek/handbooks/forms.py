from django.forms import ModelForm

from .models import HandBook, Item


class HandBookForm(ModelForm):
    """Форма для справочников."""

    class Meta:
        model = HandBook
        fields = ('text', 'name', 'description', 'version',)


class ItemForm(ModelForm):
    """Форма для элементов справочника."""

    class Meta:
        model = Item
        fields = ('code', 'value',)
