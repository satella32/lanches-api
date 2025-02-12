from rest_framework import serializers
from api_lanches.models import Cliente, Produto, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = '__all__'

    def get_total(self, obj):
        return obj.calcular_total()