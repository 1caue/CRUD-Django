from django.db import models

class categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
           return self.nome
    
class transacao(models.Model):
      data = models.DateField()
      descricao = models.CharField(max_length=200)
      valor = models.DecimalField(max_digits=7, decimal_places=7)
      category = models.ForeignKey(categoria, on_delete=models.CASCADE)
      observacoes = models.TextField()
      
      class Meta:
            verbose_name_plural = 'Transações'

      def __str__(self):
            return self.descricao