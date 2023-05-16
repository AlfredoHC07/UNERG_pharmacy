from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .permissions import create_groups_and_permissions

@receiver(post_migrate)
def create_migrations_permissions(sender, **kwargs):
    # Crear grupos de permisos para cada tipo de usuario
    create_groups_and_permissions()