# Generated by Django 5.2.1 on 2025-05-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0007_alter_inventory_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='location',
            field=models.CharField(choices=[('executive_office', 'Executive Office'), ('sales_department', 'Sales Department'), ('r&d_department', 'R&D Department'), ('it_department', 'IT department'), ('reception', 'Reception'), ('storage', 'Storage'), ('other', 'Other')], default='other', max_length=255, verbose_name='Item present location'),
        ),
    ]
