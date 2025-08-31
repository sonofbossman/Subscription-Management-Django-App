from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
  """
  Custom permission:
    - Admin users can access everything.
    - Normal users can only access their own instances.
  """

  def has_object_permission(self, request, view, obj):
    if request.user and request.user.is_staff:
      return True
    return bool(obj.user == request.user)

class IsAdminOrReadOnly(permissions.BasePermission):
  """
  Custom permission:
    - Admin users can access everything.
    - Normal users can only have read access.
  """
  
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True
    return bool(request.user and request.user.is_staff)