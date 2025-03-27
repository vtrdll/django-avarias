from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from avarias.models import Avaria, AvariaInventory
from django.db.models import Sum



def avaria_update_inventory():
    avarias_count = Avaria.objects.all().count()
    avarias_value = Avaria.objects.aggregate(
        total_value = Sum('valor')
    )['total_value']
    AvariaInventory.objects.create(
        avarias_count = avarias_count, avarias_value = avarias_value
    )

@receiver(post_save,sender = Avaria)
def avaria_post_save(sender, instance, **kwargs):
    avaria_update_inventory()


@receiver(post_delete, sender=Avaria)
def avaria_count_post_delete(sender, instance, **kwargs):
    
    avaria_update_inventory()
    


@receiver(pre_save, sender = Avaria)
def avaria_pre_save(sender, instance, **kwargs):
    if not instance.descricao:
        instance.descricao = 'bio gerada automaticamente'
