from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Product, Category


def home(request):
    return HttpResponse('Hello World')


def product_list_view(request):
    category = request.GET.get('category')

    queryset = Product.objects.filter(category__name__iexact=category) if category else Product.objects.all()

    max_price = request.GET.get('price')
    if max_price:
        queryset = queryset.filter(price__lt=max_price)

    products = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category.name,
        }
        for product in queryset
    ]

    return JsonResponse({'products': products})


def product_create_view(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    category_id = request.POST.get('category_id')

    product = Product(
        name=name,
        description=description,
        price=price,
    )

    category = Category.objects.filter(id=category_id).first()
    product.category = category
    product.save()

    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category': category.name,
    }

    return JsonResponse(product_data)


def product_delete_view(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponse('Product deleted successfully')


def product_update_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()

    if not product:
        return JsonResponse({'error': 'Product not found'})

    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    category_id = request.POST.get('category_id')

    if name:
        product.name = name
    if description:
        product.description = description
    if price:
        product.price = price
    if category_id:
        category = Category.objects.filter(id=category_id).first()
        if category:
            product.category = category

    product.save()

    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category': product.category.name,
    }
    return JsonResponse(product_data)


def category_list_view(request):
    data = Category.objects.all()
    categories = [
        {
            'id': category.id,
            'name': category.name,
            'description': category.description,
        }
        for category in data
    ]

    return JsonResponse({'categories': categories})


def category_create_view(request):
    name = request.POST.get('name')
    description = request.POST.get('description')

    fetched_category = Category.objects.filter(name=name).first()

    if fetched_category:
        return JsonResponse({'error': 'Category name should be unique'})

    category = Category(
        name=name,
        description=description,
    )
    category.save()
    return JsonResponse({'category': category})
