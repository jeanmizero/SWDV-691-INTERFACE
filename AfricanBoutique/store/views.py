from django.shortcuts import render


# Homepage
def home(request):
    return render(request, 'home.html')

# Aboutpage
def productPage(request):
    return render(request, 'product.html')
    

# Create your views here.
