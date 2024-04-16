from rest_framework.permissions import BasePermission

class IsAdminOrSuperAdmin(BasePermission):
    """
    Custom permission to allow access only to Admin or SuperAdmin users.
    """

    def has_permission(self, request, view):
        # Check if the user is an Admin or SuperAdmin
        return request.user and (request.user.is_superuser or request.user.is_staff)

class IsTeacher(BasePermission):
    """
    Custom permission to allow access only to Teacher users.
    """

    def has_permission(self, request, view):
        # Check if the user is a Teacher
        return request.user and request.user.role == 'teacher'

class IsStudent(BasePermission):
    """
    Custom permission to allow access only to Student users.
    """

    def has_permission(self, request, view):
        # Check if the user is a Student
        return request.user and request.user.role == 'student'
