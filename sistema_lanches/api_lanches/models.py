from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(unique=True, max_length=255)
    endereco = models.TextField()
    #historico_pedidos

    #def __str__(self):
        #return f"Nome: {self.nome} \nCPF: {self.cpf} \nEndereço: {self.endereco}"

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    #def __str__(self):
        #return f"Nome: {self.nome} \nPreço: {self.preco}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    tipo_entrega = models.CharField(max_length=255)
    #total = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    #def __str__(self):
        #return f"Cliente: {self.cliente} \nProdutos: {self.produtos} \nTipo de entrega: {self.tipo_entrega} \nTotal: {self.total}"
