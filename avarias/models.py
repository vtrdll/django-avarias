from django.db import models

# Create your models here.


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    industria = models.CharField (max_length=50)
    

    def __str__(self):
        return self.name

class Avaria(models.Model):

    VOLTAGEM_CHOICES = (('127','127'),('220','220'),('SEM VOLTAGEM','SEM VOLTAGEM'))


    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='Avaria_brand')
    value = models.FloatField(blank=False, null=False)
    voltagem = models.CharField(max_length=30,choices=VOLTAGEM_CHOICES, default='SEM VOLTAGEM')
    nf = models.IntegerField(blank=True, null= True)
    photo = models.ImageField(upload_to='avarias/', blank = True, null=True )
    descricao = models.TextField(blank = True, null= True)
    

    def __str__(self):
        return self.model

class AvariaInventory(models.Model):
    avarias_count = models.IntegerField()
    avarias_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.avarias_count} - {self.avarias_value}'