from django.urls import path 
from .views import ProductListView,ProductFilterView

app_name="products"
urlpatterns=[
    path("",ProductListView.as_view(),name='products'),
    path("filter/",ProductFilterView.as_view(),name="product-filter")
]