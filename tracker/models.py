from django.db import models
from django.contrib.auth.models import User

class FinancialRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notion_id = models.CharField(max_length=255, unique=True)  # Unique Notion ID
    date = models.DateField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount}"
