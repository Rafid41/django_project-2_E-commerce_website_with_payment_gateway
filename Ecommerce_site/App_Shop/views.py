from django.shortcuts import render

# import views
from django.views.generic import ListView, DetailView

#Models
from App_Shop.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# display products
class Home(ListView):
    # NOTE: ListView e context hisebe object_name set na korle by default 'object_list' name edata pass hy template e
    model = Product
    template_name = 'App_Shop/home.html'



class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'