from django.db import models

class NightClass(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Duration in weeks")
    time = models.CharField(max_length=20, help_text="Format: '(x)pm - (y)pm'")
    start_date = models.DateField(help_text="Format: 'Weekday Date# CalendarMonth'")
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    additional_notes = models.TextField(blank=True, null=True)
    optional_tag = models.CharField(max_length=100, blank=True, null=True)
    sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.name
