from django.db import models
from django.contrib.auth.models import User

DEPARTMENT_CHOICES = [
    ('r&n', 'R&D'),
    ('it', 'IT'),
    ('sales', 'Sales'),
    ('marketing', 'Marketing'),
    ('procurement', 'Procurement'),
    ('finance', 'Finance'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    employee_id = models.CharField(max_length=50, unique=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    employee_email = models.EmailField(max_length=50)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)

    def save(self, *args, **kwargs):
        # Convert to uppercase before saving
        self.employee_id = self.employee_id.upper()
        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['employee_id']),
        ]
