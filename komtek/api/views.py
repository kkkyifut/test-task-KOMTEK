from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, serializers, status, viewsets

from handbooks.models import HandBook
from .serializers import HandBookSerializer, ItemSerializer


class HandBookViewSet(viewsets.ModelViewSet):
    queryset = HandBook.objects.all()
    serializer_class = HandBookSerializer
    # permission_classes = (IsModeratorOrAuthorOrReadOnly,)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    # permission_classes = (IsModeratorOrAuthorOrReadOnly,)

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
