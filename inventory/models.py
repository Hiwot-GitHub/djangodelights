from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField()
    
    def __str__(self):
        return self.name+"Available Qty: "+ str(self.quantity)+" "+ str(self.unit)
    
    
class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    
    def __str__(self):
        return self.title +"price: "+ str(self.price)
    

class RecipeRequiremen(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    
    def __str__(self):
        return str(self.quantity) + " " + self.ingredient.unit +" of "+ self.ingredient.name +"for making "+ self.menu_item.title
    

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

