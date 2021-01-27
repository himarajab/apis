from rest_framework import permissions


class IsOwner(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
      print(vars(self))
      
      return obj.owner == request.user