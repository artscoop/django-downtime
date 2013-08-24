from downtime.models import Period
from django.contrib import admin

class PeriodAdmin(admin.ModelAdmin):
    # Scheduled downtime admin configuration
    list_select_related = True
    list_display = ['id', 'enabled', 'start_time', 'end_time']
    list_filter = ['enabled']
    search_fields = []
    actions = []
    save_on_top = False
    actions_on_top = True

admin.site.register(Period, PeriodAdmin)
