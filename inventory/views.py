from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from inventory.models import Ingredient, MenuItem, RecipeRequiremen, Purchase
from .forms import MenuItemCreateForm, IngredientCreateForm, IngredientUpdateForm,RecipeRequiremenCreateForm, PurchaseCreateForm

# Create your views here.
def home(request):
    context = {'name': 'django delights'}
    return render(request, 'inventory/home.html', context)

#list views
class MenuItemList(ListView):
    model = MenuItem
    
class IngredientList(ListView):
    model = Ingredient
    
class RecipeRequiremenList(ListView):
    model = RecipeRequiremen
    
class PurchaseList(ListView):
    model = Purchase

#Create views
class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    template_name = 'inventory/menuitem_create_form.html'
    

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = 'inventory/meuitem_create_form.html'
    
class IngredientUpdateView(CreateView):
    model = Ingredient
    form_class = IngredientUpdateForm
    template_name = 'inventory/ingredient_update_form.html'
    
    
class RecipeRequiremenCreateView(CreateView):
    model = RecipeRequiremen
    form_class = RecipeRequiremenCreateForm
    template_name = 'inventory/reciperequiremen_create_form.html'

    
class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseCreateForm
    template_name = 'inventory/purchase_create_form.html'
    

    


    

