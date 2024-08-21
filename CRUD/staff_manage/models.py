from django.db import models

CHOICES = [
    ('ICT','ICT'),
    ('I&C','I&C'),
    ('BSC','BSC'),
    ('AGED','AGED'),
]

class Staff(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    department=models.CharField(max_length=20,choices=CHOICES)

    def __str__(self):
        return f'{self.fname} {self.lname}'        