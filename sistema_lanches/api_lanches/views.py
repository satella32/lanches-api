from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from api_lanches.models import *
from api_lanches.serializers import *

# Create your views here.

#Cliente
@api_view(['GET', 'POST'])
def listar_clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def detalhe_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def historico_pedidos(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    pedidos = cliente.pedidos.all()
    serializer = PedidoSerializer(pedidos, many=True)
    return Response(serializer.data)
    

#Produto
@api_view(['GET', 'POST'])
def listar_produtos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


#Pedido
@api_view(['GET', 'POST'])
def listar_pedidos(request):
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def detalhe_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    
    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
