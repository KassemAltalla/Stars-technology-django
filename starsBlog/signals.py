from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def update_category_post_count_on_save(sender, instance, **kwargs):
    instance.category.update_post_count()

@receiver(post_delete, sender=Post)
def update_category_post_count_on_delete(sender, instance, **kwargs):
    instance.category.update_post_count()