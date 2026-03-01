from django.db import models
from django.contrib.auth.models import User


class Decision(models.Model):
    CATEGORY_CHOICES = [
        ("product", "Product Purchase"),
        ("hiring", "Hiring"),
        ("travel", "Travel Decision"),
        ("financial", "Financial"),
        ("technology", "Technology Stack"),
        ("career", "Career"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,default="other")
    context = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.context


class Option(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE, related_name="options")
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Result(models.Model):
    decision = models.OneToOneField(Decision, on_delete=models.CASCADE)
    chosen_option = models.CharField(max_length=500)
    reason = models.TextField(blank=True)
    total_score = models.IntegerField(default=0)