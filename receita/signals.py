# receitas/signals.py
import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Receita


@receiver(post_delete, sender=Receita)
def delete_imagem_ao_apagar_receita(sender, instance, **kwargs):
    if instance.imagem:
        if os.path.isfile(instance.imagem.path):
            os.remove(instance.imagem.path)
            
@receiver(pre_save, sender=Receita)
def delete_imagem_antiga_ao_atualizar(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_image = Receita.objects.get(pk=instance.pk).imagem
    except Receita.DoesNotExist:
        return

    new_image = instance.imagem
    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
