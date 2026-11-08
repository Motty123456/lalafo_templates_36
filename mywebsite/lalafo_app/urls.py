from .views import CategoryViews, ProductListViews,ProductDetailView, ProductCreateView,ProductUpdateView, ProductDeleteView
from django.urls import path


urlpatterns = [
    path('category/', CategoryViews.as_view(), name='category_list'),
    path('product/', ProductListViews.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]