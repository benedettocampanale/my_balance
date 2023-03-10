from django.contrib import admin

from .models import Label, CashFlow


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ['label__name']
    search_fields = [
        'description',
        'amount',
    ]
    list_display = [
        '__str__',
        'user',
        'label',
        'amount',
        'flow_date',
        'created_at',
        'description',
    ]
