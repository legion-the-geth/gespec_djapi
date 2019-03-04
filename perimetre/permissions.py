from rest_framework import permissions


class ManagerPerimOrReadOnly(permissions.BasePermission):
    """
    Permission qui n'autorise que les managers d'un périmètre de le modifier. 
    Sinon, lecture seule.
    """
    def has_object_permission(self, request, view, obj):
        # La lecture est autorisée pour toutes les requetes.
        if request.method in permissions.SAFE_METHODS:
            return True

        # L'écriture n'est autorisée que pour le(s) manager(s) du périmètre
        return obj.manager == request.user