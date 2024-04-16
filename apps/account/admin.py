from django.contrib import admin
from .models import User
from .models.student_profile import StudentProfile
from .models.staff_profile import StaffProfile
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm

class UserAdmin(admin.ModelAdmin):
    change_password_form = AdminPasswordChangeForm

    ordering = ['username']
    list_display = ('username', 'roles', 'is_superuser')
    search_fields = ('username','roles',)
    list_filter = ('roles', 'is_superuser')


admin.site.register(Permission)
admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(StaffProfile)