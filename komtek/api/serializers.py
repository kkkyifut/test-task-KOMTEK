from rest_framework import serializers

from handbooks.models import HandBook, Item


class HandBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = HandBook
        fields = '__all__'
        read_only_fields = ('id', 'pub_date',)


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ('id', 'handbook_id',)
