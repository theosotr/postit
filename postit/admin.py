from django.contrib import admin
from .models import Team
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Student.all_students
        return Student.objects.all()

admin.site.register(Team)
admin.site.register(Student, StudentAdmin)
# Register your models here.
