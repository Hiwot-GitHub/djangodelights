from django import forms
from .models import MenuItem, Ingredient, RecipeRequiremen, Purchase

#Create forms
class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('title','price')
        
class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name','quantity','unit','unit_price')
        
class RecipeRequiremenCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequiremen
        fields = ('menu_item', 'ingredient','quantity')

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item',)
        
#Update forms     
class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name','quantity','unit','unit_price')
        

