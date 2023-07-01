from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/list', views.MenuItemList.as_view(), name='menu'),
    path('ingredient/list', views.IngredientList.as_view(), name='ingredient'),
    path('recipereq/list', views.RecipeRequiremenList.as_view(), name='recipeReq'),
    path('recipereq/list', views.MenuItemList.as_view(), name='recipeReq'),
    path('purchase/list', views.MenuItemList.as_view(), name='purchase'),
    path('menu/create',views.MenuItemCreateView.as_view(), name="menucreate"),
    path('ingredient/create', views.IngredientCreateView.as_view(), name='ingredientcreate'),
    path('ingredient/update', views.IngredientUpdateView.as_view(), name='ingredientudate'),
    path('recipereq/create', views.RecipeRequiremenCreateView.as_view(), name='recipereq'),
    path('purchase/create', views.PurchaseCreateView.as_view(),name='purchase'), 
    
]
