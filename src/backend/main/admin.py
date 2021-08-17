from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.http import HttpResponse
from .models import Product

# Register your models here.
admin.site.register(Product)


# Set get_url with static template in admin page
# @admin.register(Person)
# class MyModelAdmin(admin.ModelAdmin):
#     change_list_template = "entities/heroes_changelist.html"
#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             path('my_view/', self.admin_site.admin_view(self.my_view)),
#         ]
#         return my_urls + urls

#     def my_view(self, request):
#         context = dict(
#            # Include common variables for rendering the admin template.
#            self.admin_site.each_context(request),
#            # Anything else you want in the context...
#            key='value',
#         )
#         return TemplateResponse(request, "admin/sometemplate.html", context)