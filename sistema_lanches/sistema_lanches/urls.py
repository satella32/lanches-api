"""
URL configuration for sistema_lanches project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api_lanches import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', views.listar_clientes, name='lista-de-clientes'),
    path('clientes/<int:pk>/', views.detalhe_cliente, name='detalhes-do-cliente'),

    path('produtos/', views.listar_produtos, name='lista-de-produtos'),
    path('produtos/<int:pk>/', views.detalhe_produto, name='detalhes-do-produto'),

    path('pedidos/', views.listar_pedidos, name='lista-de-pedidos'),
    path('pedidos/<int:pk>/', views.detalhe_pedido, name='detalhes-do-pedido'),

]
