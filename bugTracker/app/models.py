from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):

    name = models.CharField(max_length=150, db_index=True)
    description = models.TextField(max_length=600)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Enum choices for Ticket Status
class TicketStatus(models.TextChoices):
    OPEN = "open", "Open"
    IN_PROGRESS = "in_progress", "In Progress"
    RESOLVED = "resolved", "Resolved"
    CLOSED = "closed", "Closed"


# Enum choices for Ticket Priority
class TicketPriority(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    CRITICAL = "critical", "Critical"


class Ticket(models.Model):

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tickets"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TicketStatus.choices,
        default=TicketStatus.OPEN,
        db_index=True,
    )
    priority = models.CharField(
        max_length=20, choices=TicketPriority.choices, default=TicketPriority.MEDIUM
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tickets_created"
    )
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.title} - {self.status}"