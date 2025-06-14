from django.contrib import admin
from .models import Fruit

# Register your models here.
class FruitAdmin(admin.ModelAdmin):
    list_filter = ['name', 'color', 'calories', 'cost']
    search_fields = ['name', 'color', 'calories', 'cost']
    list_display = ['name', 'calories', 'cost']
admin.site.register(Fruit, FruitAdmin)
