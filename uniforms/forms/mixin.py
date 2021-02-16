class PermissionMixin:
    def get_permissions(self):
        return [permission() for permission in self.permissions_by_action.get(self.action, self.permission_classes)]