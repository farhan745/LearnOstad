from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    roll = models.IntegerField(unique=True, verbose_name="Roll Number")
    age = models.IntegerField(null=True, verbose_name="Age")
    father_name = models.CharField(
        max_length=100, verbose_name="Father Name", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}, {self.roll}"
