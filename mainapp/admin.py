from django import forms

from django.contrib import admin

from .models import *


class NotebookCategoryChoiceFiled(forms.ModelChoiceField):

    pass


class NotebookAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # При добавление ноутбука в категориях выводим только категорию ноутбуки
        if db_field.name == 'category':
            return NotebookCategoryChoiceFiled(Category.objects.filter(slug="notebooks"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneCategoryChoiceFiled(forms.ModelChoiceField):

    pass


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # При добавление смартфона в категориях выводим только категорию смартфоны
        if db_field.name == 'category':
            return SmartphoneCategoryChoiceFiled(Category.objects.filter(slug="smartphones"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Customer)