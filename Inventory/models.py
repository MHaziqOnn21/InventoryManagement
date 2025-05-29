from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('furniture', 'Furniture'),
    ('stationery', 'Stationery'),
    ('computer_accesories', 'Computer Accesories'),
    ('operational_equiment', 'Operational Equiment'),
    ('r&d_equipment', 'R&D Equipment'),
    ('other', 'Other'),
]

LOCATION_CHOICES = [
    ('executive_office', 'Executive Office'),
    ('hr_department', 'HR Department'),
    ('finance_department', 'Finance Department'),
    ('sales_department', 'Sales Department'),
    ('r&d_department', 'R&D Department'),
    ('it_department', 'IT department'),
    ('reception', 'Reception'),
    ('storage', 'Storage'),
    ('other', 'Other'),
]

CONDITION_CHOICES = [
    ('new', 'New'),
    ('like_new', 'Like New'),
    ('excellent', 'Excellent'),
    ('good', 'Good'),
    ('fair', 'Fair'),
    ('used', 'Used'),
    ('needs_repair', 'Needs Repair'),
    ('poor', 'Poor'),
    ('damaged', 'Damaged'),
    ('scrap', 'Scrap'),
]

ASSIGNED_TO_CHOICES = [
    ('null', 'null'),
    ('johndoe', 'John Doe'),
    ('janedoe', 'Jane Doe'),
    ('alicewong', 'Alice Wong'),
    ('bobsmith', 'Bob Smith'),
    ('charlielee', 'Charlie Lee'),
    ('dianatan', 'Diana Tan'),
    ('ericng', 'Eric Ng'),
    ('fionalim', 'Fiona Lim'),
    ('georgeho', 'George Ho'),
    ('hannahcho', 'Hannah Cho'),
    ('jadefox', 'Jade Fox'),
    ('ivyclarke', 'Ivy Clarke'),
    ('novasilver', 'Nova Silver'),
    ('echoryder', 'Echo Ryder'),
    ('blakecrimson', 'Blake Crimson'),
    ('lunatrace', 'Luna Trace'),
    ('ashforge', 'Ash Forge'),
    ('rexblaze', 'Rex Blaze'),
    ('zanequantum', 'Zane Quantum'),
    ('neocipher', 'Neo Cipher'),
]

INTENDED_USAGE_CHOICES = [
    ('null', 'null'),
    ('finance', 'Finance'),
    ('human_resources', 'Human Resources'),
    ('sales', 'Sales'),
    ('operation', 'Operation'),
    ('r&d', 'R&D'),
    ('software_development', 'Software Development'),
    ('administration', 'Administration'),
    ('other', 'Other'),
]

class Inventory(models.Model):
    name = models.CharField(verbose_name='Item name', max_length=255, default="null")
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='other')
    ser_number = models.CharField(verbose_name='Serial numbers', default="null", max_length=255)
    tag_number = models.CharField(verbose_name='Tag numbers', default="null", max_length=255)
    quantity = models.IntegerField(verbose_name='Quantity', default=1)
    description = models.TextField(verbose_name="Description", max_length=800, default="null")
    location = models.CharField(verbose_name='Item present location', max_length=255, choices=LOCATION_CHOICES, default='other')
    d_o_p = models.DateField(verbose_name='Date Of Purchase (YYYY-MM-DD)', null=True, blank=True)
    purchase = models.DecimalField(verbose_name='Purchased price', null=True, blank=True, max_digits=10, decimal_places=2)
    vendor = models.CharField(verbose_name='Seller', default="null", max_length=255)
    receipt = models.ImageField(verbose_name='Receipt', upload_to='receipts/', null=True, blank=True)
    condition = models.CharField(verbose_name='Asset condition', max_length=50, choices=CONDITION_CHOICES, default='good')
    assigned_to = models.CharField(verbose_name='Assigned to who?', max_length=255, choices=ASSIGNED_TO_CHOICES, default='other')
    intended_usage = models.CharField(verbose_name='Purpose of assigned item', choices=INTENDED_USAGE_CHOICES, default="null", max_length=255)
    additional_notes = models.TextField(verbose_name='Additional notes', default="null", max_length=800)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True,)
    updated_by = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='updated_inventories'
    )

    created_by = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_inventories'
    )

    def __str__(self):
        return f"{self.name} - Assigned to: {self.assigned_to}"