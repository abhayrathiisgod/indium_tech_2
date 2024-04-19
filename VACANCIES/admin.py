from django.contrib import admin
from .models import Jobs, Candidates


# Register your models here.


class JobsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Title', 'Open_date',
                    'Close_date', 'Created_at', 'Updated_at')
    list_filter = ('Title', 'Job_name', 'Open_date',
                   'Close_date', 'Created_at', 'Updated_at')
    list_display_links = ('Id', 'Title', 'Open_date',
                          'Close_date', 'Created_at', 'Updated_at')


class CandidatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Email', 'Position', 'Created_at')
    list_filter = ('Name', 'Email', 'Position', 'Created_at')
    list_display_links = ('id', 'Name', 'Email', 'Position', 'Created_at')


admin.site.register(Jobs, JobsAdmin)
admin.site.register(Candidates, CandidatesAdmin)
