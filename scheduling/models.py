from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ('candidate', 'Candidate'),
        ('interviewer', 'Interviewer'),
    )
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.user.name}: {self.start_time} - {self.end_time} on {self.date}"
