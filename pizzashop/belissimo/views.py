from django.shortcuts import render, redirect
from .models import *
from .forms import *
from cart.cart import Cart
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# @login_required(login_url='login')
def home_page(request):
    category = Category.objects.all()
    products = Product.objects.all()

    context = {
        'category': category,
        'products': products,
    }
    page = 'mainapp/index.html'

    return render(request, page, context)


def menu_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    get_req = request.POST.get('category_id')

    if request.method == "POST" and get_req:
        products = Product.objects.filter(category=get_req)

    context = {
        'categories': categories,
        'products': products,
    }

    page = 'mainapp/menu.html'
    return render(request, page, context)


def contact_page(request):
    page = 'mainapp/contact.html'
    return render(request, page)


# @login_required(login_url="login")
def cart_detail(request):
    page = 'mainapp/cart.html'
    return render(request, page)


def services_page(request):
    page = 'mainapp/services.html'
    return render(request, page)


def blog_page(request):
    page = 'mainapp/blog.html'
    return render(request, page)


def about_page(request):
    page = 'mainapp/about.html'
    return render(request, page)


def single_page(request):
    page = 'mainapp/blog_single.html'
    return render(request, page)


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                # user = form.cleaned_data.get('username')
                return redirect('login')

        context = {'form': form}

        page = 'mainapp/registration.html'

        return render(request, page, context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "ERORR")

        context = {}

        return render(request, 'mainapp/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("menu")


# @login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


# @login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


# @login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


# @login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    page = 'mainapp/index.html'

    context = {
        'form': form,
    }
    return render(request, page, context)