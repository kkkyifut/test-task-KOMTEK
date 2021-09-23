from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import HandBook, Item


def index(request) -> HttpResponse:
    """view-функция для главной страницы."""
    return render(request, 'index.html')


def handbooks(request) -> HttpResponse:
    """view-функция для просмотра всех справочников."""
    handbooks = HandBook.objects.all()
    paginator = Paginator(handbooks, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page}
    return render(request, 'handbooks/handbooks.html', context)


def handbook_view(request, handbook_id) -> HttpResponse:
    """view-функция для просмотра справочника."""
    handbook = get_object_or_404(HandBook, id=handbook_id)
    items = Item.objects.filter(handbook=handbook)
    paginator = Paginator(items, 20)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'handbook': handbook, 'page': page}
    return render(request, 'handbooks/handbook.html', context)


def page_not_found(request, exception) -> HttpResponse:
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request) -> HttpResponse:
    return render(request, 'misc/500.html', status=500)
