from django.contrib import admin

from app.models import JobPost, Location, Skills, Author


class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date', 'expiry')
    list_filter = ('date', 'salary')
    search_fields = ('title', 'description')
    search_help_text = "Search by title or description"
    # fields = (('title', 'description',), 'salary', 'expiry')
    # exclude = ('slug',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description')
        }),
        ('More Information', {
            'classes': ('collapse', 'wide',),
            'fields': (('salary', 'expiry'), 'slug')
        }),
    )


# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Skills)
admin.site.register(Author)
