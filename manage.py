from django.db import models


# Michael Was Here

class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class MaintenanceTask(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    steps = models.TextField()
    tools_required = models.TextField()
    parts_required = models.TextField()
    estimated_time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.task_name} for {self.vehicle}"
