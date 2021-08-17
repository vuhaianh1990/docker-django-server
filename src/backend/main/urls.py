from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    # path('', TemplateView.as_view(template_name='page/home.html'), name='home')
    path("", index, name="homepage")
]
