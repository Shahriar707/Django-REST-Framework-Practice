from rest_framework import permissions
from .permissions import IsEditorPermission

class EditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsEditorPermission]
    
class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False 
    def get_queryset(self, *args, **kwargs):
        user = self.request.user 
        lookup_data = {}
        lookup_data[self.user_field] = user 
        qs = super().get_queryset(*args, **kwargs)
        if user.is_staff:
            return qs 
        return qs.filter(**lookup_data)