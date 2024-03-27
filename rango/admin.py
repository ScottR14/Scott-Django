from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(UserProfile)
