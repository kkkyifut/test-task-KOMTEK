from django.urls import path

from . import views

app_name = 'handbooks'

urlpatterns = [
    path('', views.index, name='index'),
    path('handbooks/', views.handbooks, name='handbooks'),
    path('handbooks/<int:handbook_id>/',
         views.handbook_view, name='handbook_view'),
]
