from django.shortcuts import render 

def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def checkout(request):
    return render(request, 'website/checkout.html')

def contact(request):
    return render(request, 'website/contact.html')

def shop(request):
    return render(request, 'website/shop.html')

def shopingcart(request):
    return render(request, 'website/shopingcart.html')