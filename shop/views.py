from django.shortcuts import render

def shop(request):
    return render(request,'shop.html')

def shopdetails(request):
    return render(request,'shopdetails.html')

def shopingcart(request):
    return render(request,'shopingcart.html') 