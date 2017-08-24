from django.conf.urls import url
from django.contrib import admin
from home.views import get_index, do_search
from products import urls as products_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='index'),    
    url(r'^search/', do_search, name='search'),
    url(r'products/', include(products_urls)),
]