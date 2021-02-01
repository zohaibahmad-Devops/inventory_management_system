
from django.shortcuts import render
from django.contrib import messages
from inventory_management_system.models import InputProduct, Expenses


def index_view(request):
    return render(request, 'index.html')


def bill_view(request):
    products = InputProduct.objects.all()

    context = {
        'products': products
    }

    return render(request, 'bill.html' , context=context)


# def login_view(request):
#     if request.method == "POST":
#         user_name = request.POST.get('user_name')
#         password = request.POST.get('password')
#         login = Login.objects.create(user_name=user_name, password=password)
#         messages.success(request, 'Your are Successfully Login')
#
#     return render(request, 'login.html')


def input_product_view(request):
    if request.method == "POST":
        category = request.POST.get('category')
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        receive_by = request.POST.get('receive_by')
        price_in = request.POST.get('price_in')
        price_out = request.POST.get('price_out')
        last_update = request.POST.get('last_update')
        input_product = InputProduct.objects.create(category=category, item_name=item_name, quantity=quantity,
                                                    receive_by=receive_by, price_in=price_in, price_out=price_out,
                                                    last_update=last_update)
        messages.success(request, 'You have entered your stock successfully')

    return render(request, "addproduct.html")


def expenses_view(request):
    if request.method == "POST":
        rent = request.POST.get('rent')
        gas_bill = request.POST.get('gas_bill')
        electricity_bill = request.POST.get('electricity_bill')
        maintenance = request.POST.get('maintenance')
        staff_salaries = request.POST.get('staff_salaries')
        expenses = Expenses.objects.create(rent=rent, gas_bill=gas_bill, electricity_bill=electricity_bill,
                                           maintenance=maintenance, staff_salaries=staff_salaries)
        messages.success(request, 'You have entered your expenses successfully')

    return render(request, "expenses.html")
