# Generated by Django 4.1.7 on 2023-03-06 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Label name', max_length=255)),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
            },
        ),
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, help_text='Can be negative', max_digits=10)),
                ('flow_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=255)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cash_flows', to='cash_flow.label')),
            ],
            options={
                'verbose_name': 'Cash Flow',
                'verbose_name_plural': 'Cash Flows',
            },
        ),
    ]