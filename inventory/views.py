from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from inventory.models import Ingredient, MenuItem, RecipeRequiremen, Purchase

# Create your views here.
def home(request):
    context = {'name': 'django delights'}
    return render(request, 'inventory/home.html', context)


class MenuItemList(ListView):
    model = MenuItem
    
class IngredientList(ListView):
    model = Ingredient
    
class RecipeRequiremenList(ListView):
    model = RecipeRequiremen
    
class PurchaseList(ListView):
    model = Purchase
    