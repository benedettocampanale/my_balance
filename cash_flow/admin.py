from django.contrib import admin

from .models import Label, CashFlow


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    pass
