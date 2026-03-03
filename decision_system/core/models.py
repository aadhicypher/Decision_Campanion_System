from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category.name} - {self.name}"
    
class CategoryCriterion(models.Model):
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="criteria"
    )
    name = models.CharField(max_length=200)
    default_weight = models.FloatField(default=1.0)
    is_positive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.subcategory.name} - {self.name}"



class Decision(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
    SubCategory,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.context

class Option(models.Model):
    decision = models.ForeignKey(
        Decision,
        on_delete=models.CASCADE,
        related_name="options"
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Criterion(models.Model):
    decision = models.ForeignKey(
        Decision,
        on_delete=models.CASCADE,
        related_name="decision_criteria"
    )
    name = models.CharField(max_length=200)
    weight = models.FloatField(default=1.0)
    is_positive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.decision.context} - {self.name}"

class Score(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    value = models.IntegerField()  # 1 to 5

    
class Result(models.Model):
    decision = models.OneToOneField(Decision, on_delete=models.CASCADE)
    chosen_option = models.CharField(max_length=500)
    reason = models.TextField(blank=True)
    total_score = models.IntegerField(default=0)