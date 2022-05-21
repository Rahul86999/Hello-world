from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class Addcourse(models.Model):
    course=models.CharField(max_length=200)
    fees=models.IntegerField(default=170)
    duratoin=models.CharField(max_length=50)

    def __str__(self):
        return self.course

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class Studentmodel(models.Model):
    roll_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    age = models.IntegerField()
    mobile_no = models.IntegerField()
    course = models.ForeignKey(Addcourse, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self. name

class Payfee(models.Model):
    course = models.ForeignKey(Addcourse, on_delete=models.CASCADE)
    deposit=models.CharField(max_length=50)
    panding_fee = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.course

