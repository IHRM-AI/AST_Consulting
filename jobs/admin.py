from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'company', 'location', 'salary', 'rating')
    search_fields = ('position_name', 'company', 'location')

admin.site.site_header = "Job Portal Admin"
admin.site.site_title = "Job Management"
admin.site.index_title = "Manage Jobs"
