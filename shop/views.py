from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import ProductGroup, Product
from .recommender import Recommender


def product_list(request, category_slug=None):
    category = None
    categories = ProductGroup.objects.all()
    products = Product.objects.filter(accessible=True)

    if category_slug:
        category = get_object_or_404(ProductGroup, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, accessible=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    return render(request, 'shop/product/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'recommended_products': recommended_products
    })
