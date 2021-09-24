from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from handbooks.models import HandBook

from .serializers import HandBookSerializer, ItemSerializer


class HandBookViewSet(viewsets.ModelViewSet):
    queryset = HandBook.objects.all()
    serializer_class = HandBookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ('get', 'head', 'options',)
    pagination_class = PageNumberPagination


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ('get', 'head', 'options',)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        handbook = get_object_or_404(
            HandBook, id=self.kwargs['handbook_id'],
        )
        return handbook.items.all()

    def perform_create(self, serializer):
        handbook = get_object_or_404(
            HandBook, id=self.kwargs['handbook_id'],
        )
        serializer.save(handbook=handbook)
