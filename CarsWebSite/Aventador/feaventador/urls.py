from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('iletisim', views.contact, name="contact"),
    path('<slug:slug>', views.page_detail_view, name="page_detail"),
]