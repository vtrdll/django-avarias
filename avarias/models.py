from django.db import models

# Create your models here.


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    industria = models.CharField (max_length=50)
    

    def __str__(self):
        return self.industria

class Avaria(models.Model):

    VOLTAGEM_CHOICES = (('127 VOLTS','127 VOLTS'),('220 VOLTS','220 VOLTS'),('SEM VOLTAGEM','SEM VOLTAGEM'))


    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=200)
    marca = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='Avaria_brand')
    valor = models.FloatField(blank=False, null=False)
    voltagem = models.CharField(max_length=30,choices=VOLTAGEM_CHOICES, default='SEM VOLTAGEM')
    nota_fiscal = models.IntegerField(blank=True, null= True)
    descricao = models.TextField(blank = True, null= True)
    

    def __str__(self):
        return self.modelo

class AvariaInventory(models.Model):
    avarias_count = models.IntegerField()
    avarias_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.avarias_count} - {self.avarias_value}'
    
class ImagemReferencia(models.Model):
    avaria = models.ForeignKey(Avaria, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='avarias/')
    

    def __str__(self):
        return f"Imagem para a avaria {self.avaria.id}"