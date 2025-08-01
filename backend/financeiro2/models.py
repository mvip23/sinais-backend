from django.db import models

class Receita(models.Model):
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Receita: {self.descricao} - R$ {self.valor}"

class Despesa(models.Model):
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Despesa: {self.descricao} - R$ {self.valor}"

class AnexoComprovante(models.Model):
    despesa = models.ForeignKey(Despesa, on_delete=models.CASCADE, related_name='anexos')
    arquivo = models.FileField(upload_to='comprovantes/')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comprovante para {self.despesa.descricao}" 