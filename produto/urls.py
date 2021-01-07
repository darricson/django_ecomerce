from django.urls import path
from produto.views import home_page, new_product


urlpatterns = [

    path('', home_page, name='home'),
    path('product_new/', new_product, name='product_new'),
    
]


