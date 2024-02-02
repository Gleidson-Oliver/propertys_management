from django.db import models


class Casa(models.Model):
    foto = models.ImageField(upload_to='alugueis/covers/%Y/%m/%d/', blank=True, default='')
    cidade = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'Rua: {self.rua} -- Nº{self.numero}'



class Inquilino(models.Model):
    nome = models.CharField(max_length=255)
    casa=models.ForeignKey(Casa, on_delete=models.CASCADE, default=None)
    telefone = models.CharField(max_length=15,  unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    carne=models.FileField(upload_to='alugueis/covers/%Y/%m/%d/')
    contrato=models.FileField(upload_to='alugueis/covers/%Y/%m/%d/')
    Aluguel=models.CharField(max_length=255, default=None)
    data_vencimento = models.CharField(max_length=10, default=None)  # Adicionando unique=True

    def __str__(self):
        return f'INQUILINO: {self.nome}'





