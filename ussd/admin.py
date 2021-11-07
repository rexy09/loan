from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Sajili)
class SajiliAdmin(admin.ModelAdmin):
    '''Admin View for Sajili'''

    list_display = ('pk', 'full_name', 'phone_number',
                    'balance', 'pin', 'updated_at', 'created_at')
    list_display_links = ['pk', 'full_name', ]
    list_filter = ('created_at',)
    search_fields = ('full_name', 'phone_number',)
    ordering = ('full_name',)

admin.site.register(TumaPesa)
admin.site.register(TumaPesa1)
admin.site.register(TumaPesa2)
admin.site.register(TumaPesa3)
admin.site.register(TumaPesa4)
