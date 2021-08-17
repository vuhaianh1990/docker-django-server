from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from .views import book


urlpatterns = [
    # path('', include(router.urls)),
    # path('', TemplateView.as_view(template_name='page/home.html'), name='home')
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path("book/", book, name="book"),
]
