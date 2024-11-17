from django.shortcuts import render

from product.models import Product


def category_list(request, slug):
    products = Product.objects.select_related('category').filter(category__slug=slug).order_by('-datetime_created')
    
    context = {
        "products" : products,
    }
    
    return render(request, 'category/category_list.html', context)

