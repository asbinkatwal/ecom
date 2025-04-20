
from django.urls import path
from ecomm import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
