# Generated by Django 5.2.1 on 2025-05-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=255)),
                ('category', models.CharField(default='null', max_length=255)),
                ('ser_number', models.CharField(default='null', max_length=255, verbose_name='Serial numbers')),
                ('tag_number', models.CharField(default='null', max_length=255, verbose_name='Tag numbers')),
                ('quantity', models.IntegerField(default='1', verbose_name='Quantity')),
                ('description', models.TextField(default='null', max_length=800, verbose_name='Description')),
                ('location', models.CharField(default='null', max_length=255, verbose_name='Item present location')),
                ('d_o_p', models.DateField(default='null', verbose_name='Date Of Purchase/Date Acquired')),
                ('purchase', models.DecimalField(decimal_places=2, default='null', max_digits=10, verbose_name='Purchased price')),
                ('vendor', models.CharField(default='null', max_length=255, verbose_name='Seller')),
                ('receipt', models.ImageField(default='null', upload_to='receipts/', verbose_name='Receipt')),
                ('condition', models.CharField(default='null', max_length=50, verbose_name='Asset condition')),
                ('assigned_to', models.CharField(default='null', max_length=255, verbose_name='Assigned to who?')),
                ('intended_usage', models.CharField(default='null', max_length=255, verbose_name='Purpose of assigned item')),
                ('additional_notes', models.TextField(default='null', max_length=800, verbose_name='Additional notes')),
            ],
        ),
    ]
