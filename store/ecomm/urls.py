
from django.urls import path
from ecomm import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('cart/', views.cart_list_create, name='cart-list-create'),
    path('cart/<int:pk>/', views.cart_detail, name='cart-detail'),
    path('users/', views.user_list_create, name='user-list-create'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    path('login/', views.login_view, name='login_view'),
    path('api/activate/<uidb64>/<token>/', views.ActivateAccountAPIView.as_view(), name='activate-account'),
    path('promote-user/', views.promote_view, name='promote-user'),

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
