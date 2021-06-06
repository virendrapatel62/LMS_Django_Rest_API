from django.db import models
import uuid
from course.models import Course
import shortuuid
# Create your models here.


def random_code():
    return shortuuid.ShortUUID().random(length=6).upper()


class Coupon(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    discount = models.IntegerField()
    active = models.BooleanField(default=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='coupons')
    code = models.CharField(max_length=6,
                            null=False, default=random_code)

    def __str__(self):
        return self.code

    @classmethod
    def is_valid(cls, course, code):
        return Coupon.objects.filter(course=course, code=code, active=True).count() > 0
