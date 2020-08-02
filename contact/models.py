from django.db import models

class Contact(models.Model):
    ENQUIRT = (
        ('A general enquiry','A general enquiry'),
        ()
    )
    enquiry_type = models.CharField(max_length=100, choices=)