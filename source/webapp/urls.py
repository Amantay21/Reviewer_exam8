from django.urls import path

from webapp.views.product_views import ProductsView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from webapp.views.review_views import ReviewCreateView, \
     ReviewView, ReviewUpdateView, ReviewDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='products_detail_view'),
    path('product/create/', ProductCreateView.as_view(), name='products_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='products_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
    path('review/<int:pk>/add/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewView.as_view(), name='review_view'),
    path('review/<int:pk>/edit', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete')
]