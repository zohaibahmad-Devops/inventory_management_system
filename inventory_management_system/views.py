from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def input_product_view(request):
    return render(request, 'addproduct.html')
