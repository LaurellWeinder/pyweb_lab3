from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from .models import Product
from .settings.base import *
from django.core.paginator import Paginator

# Create your views here.

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
        blog_pages = [{'icon_chat': '18',
                       'image': 'shop/images/image_1.jpg',
                       'text': 'Some description text',
                       'date': 'March 18, 2020',
                       'author': 'John Doe',
                       'heading': 'Some heading',
                      },
                      {'icon_chat': '18',
                       'image': 'shop/images/image_2.jpg',
                       'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
                       'date': 'January 20, 2020',
                       'author': 'Admin',
                       'heading': 'Some heading',
                       },
                      {'icon_chat': '4',
                       'image': 'shop/images/image_3.jpg',
                       'heading': 'Even the all-powerful Pointing has no control about the blind texts',
                       'date': 'April 09, 2019',
                       'author': 'Admin',
                       'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
                      },
                      {'icon_chat': '10',
                       'image': 'shop/images/image_4.jpg',
                       'heading': 'Even the all-powerful Pointing has no control about the blind texts',
                       'date': 'April 20, 2019',
                       'author': 'John Doe',
                       'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
                       },
                      {'icon_chat': '3',
                       'image': 'shop/images/image_5.jpg',
                       'heading': 'Even the all-powerful Pointing has no control about the blind texts',
                       'date': 'April 20, 2019',
                       'author': 'John Doe',
                       'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
                       },
                      {'icon_chat': '6',
                       'image': 'shop/images/image_6.jpg',
                       'heading': 'Even the all-powerful Pointing has no control about the blind texts',
                       'date': 'February 20, 2019',
                       'author': 'Admin',
                       'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
                       },
                      ]
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

        
        
        
        
        
        
        
        
        
        
        
        
        
        