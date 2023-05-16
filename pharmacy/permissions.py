from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def create_groups_and_permissions():
    # Crear grupos de permisos para cada tipo de usuario
    report_user_grup = Group.objects.get_or_create(name='supervisor')[0]
