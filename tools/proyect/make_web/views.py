from django.shortcuts import render

# Create your views here.
def first_page(request):
    return render(request, 'index.html')