from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequiremen, Purchase

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequiremen)
admin.site.register(Purchase)
