from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Label(models.Model):
    name = models.CharField(max_length=255, help_text='Label name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Label'
        verbose_name_plural = 'Labels'


class CashFlow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cash_flows')
    label = models.ForeignKey("Label", on_delete=models.CASCADE, related_name='cash_flows')
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Can be negative')
    flow_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'Flow: {self.label} - {self.amount} (on {self.flow_date})'

    class Meta:
        verbose_name = 'Cash Flow'
        verbose_name_plural = 'Cash Flows'
