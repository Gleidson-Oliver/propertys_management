from django.db import models

from Alugueis.models import Inquilino

# Create your models here.

class PagamentosJaneiro(models.Model):
    inquilino=models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    agua_pago=models.BooleanField(default=False, verbose_name='MARQUE SE A CONTA DE ÁGUA FOI PAGA')
    energia_pago=models.BooleanField(default=False, verbose_name='MARQUE SE A CONTA DE ENERGIA FOI PAGA')
    aluguel_pago=models.BooleanField(default=False, verbose_name='MARQUE SE O ALUGUEL FOI PAGO')
    talao_energia=models.FileField(upload_to='janeiro/', blank=True, default='', verbose_name=' ANEXAR TALÃO DE ENERGIA PAGO')
    talao_agua=models.FileField(upload_to='janeiro/', blank=True, default='', verbose_name=' ANEXAR TALÃO DE ÁGUA PAGO')
    carne=models.FileField(upload_to='janeiro/', blank=True, default='', verbose_name=' ANEXAR CARNÊ PAGO')

    class Meta:
        verbose_name='Pagamento de Janeiro'
        verbose_name_plural='Pagamentos de Janeiro'

    
    def __str__(self):
        return f'{self.inquilino} --  -- -- Tudo Pago ' if self.energia_pago and self.agua_pago and self.aluguel_pago else f'{self.inquilino} -- -- -- Pendete de Pagamentos ' 



