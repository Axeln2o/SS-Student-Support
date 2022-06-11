from django.db import models


class Professor(models.Model):
    department_choices = (('hist', 'History'), ('math', 'Mathematics'), ('litrt', 'Literature'), ('eng', 'English'))
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=10, choices=department_choices)
    time = models.TimeField()
    # Campuri auxiliare
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
