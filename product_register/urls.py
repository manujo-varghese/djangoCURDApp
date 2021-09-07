"""Xero_manu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views

urlpatterns = [
    path('',views.product_form,name='product_insert'),
    path('<int:id>/',views.product_form,name='product_update'),
    path('delete/<int:id>/', views.product_delete, name='product_delete'),
    path('list/',views.product_list,name='product_list'),
    path('product_option_list/',views.product_option_list,name='product_option_list'),
    path('product_option_list/insert',views.product_option_form,name='product_option_insert'),
    path('product_option_list/<int:id>/', views.product_option_form, name='product_option_update'),
    path('product_option_list/delete/<int:id>/', views.product_option_delete, name='product_option_delete'),
]
