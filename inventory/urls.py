from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    # Authentication
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    # Products
    path('', views.product_list, name='product-list'),
    path('product/add/', views.add_product, name='add'),
    path('product/edit/<int:pk>/', views.edit_product, name='edit'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete'),
]