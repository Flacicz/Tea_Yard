from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout

from cart.forms import CartAddProductForm
from .forms import UserRegisterForm, UserLoginForm

from .models import *


def index(request):
    products = Products.objects.filter(available=True)

    paginator = Paginator(products, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'TeaYardApp/index.html',
                  {'products': products, 'page_obj': page_obj})


def get_category(request, category_id):
    products = Products.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    paginator = Paginator(products, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'TeaYardApp/category.html',
                  {'products': products, 'category': category, 'page_obj': page_obj})


def view_products(request, products_id):
    products_item = get_object_or_404(Products, id=products_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'TeaYardApp/view_products.html',
                  {'products_item': products_item, 'cart_product_form': cart_product_form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'TeaYardApp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'TeaYardApp/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
