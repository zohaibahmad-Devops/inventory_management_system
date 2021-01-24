from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def addproduct_view(request):
    return render(request, 'addproduct.html')
