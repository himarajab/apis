from authentication.models import User
from django.db import models

# Create your models here.
class Income(models.Model):
  SOURCE_OPTIONS=[
    ('SALARY','Salary'),
    ('BUSINESS','Business'),
    ('SIDE-HUSTLES','Side Hustles'),
    ('OTHERS','Others')
  ]

  source = models.CharField(choices=SOURCE_OPTIONS, max_length=250)
  amount = models.DecimalField(max_digits=10,decimal_places=2)
  description = models.TextField()
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField(null=False,blank=False)

  class Meta:
    ordering:['date']

  def __str__(self):
    return f"{str(self.owner)}'s income"