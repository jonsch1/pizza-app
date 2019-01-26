from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Pizza, Topping

# Create your views here.
def index(request):
    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all()
    }
    return render(request, "cart/menu.html", context=context)
