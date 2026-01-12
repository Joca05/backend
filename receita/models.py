from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    imagem = models.ImageField(upload_to='receita/upload', blank=True, null=True)


    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receita')
    categoria = models.ForeignKey(
            Categoria,  
            on_delete=models.SET_NULL,
            null=True,
            related_name='receita'
        )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def total_visualizacoes(self):
       
        return self.visualizacoes.count()



class Interacao(models.Model):
    COMENTARIO = 'COM'
    AVALIACAO = 'AVA'

    TIPO_INTERACAO = [
        (COMENTARIO, 'Comentário'),
        (AVALIACAO, 'Avaliação'),
    ]

    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='interacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=3, choices=TIPO_INTERACAO)

    comentario = models.TextField(null=True, blank=True)
    estrelas = models.IntegerField(null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
     
        if self.tipo == self.COMENTARIO:
            self.estrelas = None
        elif self.tipo == self.AVALIACAO:
            self.comentario = None

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.usuario} → {self.receita}'



class Visualizacao(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='visualizacoes')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Visualização de {self.receita.titulo} em {self.criado_em}'
