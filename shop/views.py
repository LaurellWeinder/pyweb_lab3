from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import Product, Blog
from .settings.base import *
from django.core.paginator import Paginator


class IndexView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)
        return render(request, 'shop/index.html', {'phone_number': PHONE_NUMBER,
                                                   'title': TITLE,
                                                   'email': EMAIL,
                                                   'address': ADDRESS,
                                                   'text': TEXT,
                                                   })


class ShopView(View):

    def get(self, request, page_id=1):

        products_list = Product.objects.all()

        paginator = Paginator(products_list, 12)

        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('shop'))

        return render(request, 'shop/shop.html', {'products': products,
                                                  'phone_number': PHONE_NUMBER,
                                                  'title': TITLE,
                                                  'email': EMAIL,
                                                  'address': ADDRESS,
                                                  'text': TEXT,
                                                  'date': DATE,
                                                  })


class WishlistView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/wishlist.html', {'phone_number': PHONE_NUMBER,
                                                      'title': TITLE,
                                                      'email': EMAIL,
                                                      'address': ADDRESS,
                                                      'text': TEXT,
                                                      'date': DATE,
                                                      })


class AboutView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/about.html', {'phone_number': PHONE_NUMBER,
                                                   'title': TITLE,
                                                   'email': EMAIL,
                                                   'address': ADDRESS,
                                                   'text': TEXT,
                                                   'date': DATE,
                                                   })


class BlogView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)
        blog_pages = Blog.objects.all()
        return render(request, 'shop/blog.html', {'phone_number': PHONE_NUMBER,
                                                  'title': TITLE,
                                                  'email': EMAIL,
                                                  'address': ADDRESS,
                                                  'text': TEXT,
                                                  'date': DATE,
                                                  'blog_pages': blog_pages,
                                                  })


class BlogSingleView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/blog-single.html', {'phone_number': PHONE_NUMBER,
                                                         'title': TITLE,
                                                         'email': EMAIL,
                                                         'address': ADDRESS,
                                                         'text': TEXT,
                                                         'date': DATE,
                                                         })


class CartView(View):
    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/cart.html', {'phone_number': PHONE_NUMBER,
                                                  'title': TITLE,
                                                  'email': EMAIL,
                                                  'address': ADDRESS,
                                                  'text': TEXT,
                                                  'date': DATE,
                                                  })


class CheckoutView(View):
    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/checkout.html', {'phone_number': PHONE_NUMBER,
                                                      'title': TITLE,
                                                      'email': EMAIL,
                                                      'address': ADDRESS,
                                                      'text': TEXT,
                                                      'date': DATE,
                                                      })


class ContactView(View):
    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/contact.html', {'phone_number': PHONE_NUMBER,
                                                     'title': TITLE,
                                                     'email': EMAIL,
                                                     'address': ADDRESS,
                                                     'text': TEXT,
                                                     'date': DATE,
                                                     })


class ProductSingleView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/product-single.html', {'phone_number': PHONE_NUMBER,
                                                            'title': TITLE,
                                                            'email': EMAIL,
                                                            'address': ADDRESS,
                                                            'text': TEXT,
                                                            'date': DATE,
                                                            })
