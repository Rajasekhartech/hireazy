from django.db import models

# Create your models here.

class candidates(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    current_ctc = models.IntegerField()
    expected_ctc = models.IntegerField()
    notice_period = models.IntegerField()
