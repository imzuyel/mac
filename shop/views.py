from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
	allProds=[]
	products=Product.objects.values('category','id')
	cats={item['category'] for item in products}
	for cat in cats:
		prod=Product.objects.filter(category=cat)
		n=len(prod)
		nSlides=n//4+ceil((n/4)-n//4)
		allProds.append([prod,range(1,nSlides),nSlides])
		dic={'allProds':allProds}
	return render(request,'shop/index.html',dic)


def about(request):
	return render(request,'shop/about.html')

def contact(request):
	return render(request,'shop/contact.html')

def tracker(request):
	return render(request,'shop/tracker.html')

def search(request):
	return render(request,'shop/search.html')

def productView(request):
	return render(request,'shop/productView.html')

def checkout(request):
	return render(request,'shop/checkout.html')
