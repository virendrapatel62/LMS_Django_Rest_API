from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from course.models import Course
import uuid
# Create your models here.


def rating_validation(value):
    if value > 5 or value < 1:
        raise ValidationError("rating must be between 1 to 5")


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    content = models.CharField(max_length=300)
    rating = models.IntegerField(validators=[rating_validation])
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
