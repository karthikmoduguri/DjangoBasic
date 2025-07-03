from django.shortcuts import render

# Create your views here.
def all_ecom(request):
    return render(request, 'ecom/all_ecom.html')