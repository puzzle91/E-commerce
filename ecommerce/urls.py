"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import get_index
from accounts import urls as accounts_urls
from accounts import reset_urls as reset_urls
from products import urls as products_urls
from cart import urls as cart_urls
from cart import views as cart_views
from payments import urls as payments_urls
from .settings import MEDIA_ROOT
from django.views import static
from categories import urls as categories_urls
from home.views import get_index, do_search
from search.views import product_search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='index'),
    url(r'accounts/', include(accounts_urls)),
    url(r'user/', include(reset_urls)),
    url(r'products/', include(products_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^payments/', include(payments_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^categories/', include(categories_urls)),
    url(r'^search/', do_search, name='search'),    
    url(r'^$', get_index, name='index'),
    url(r'before/', product_search, name='searchprod'),
]
