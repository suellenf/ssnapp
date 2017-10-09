from __future__ import unicode_literals

from django.db import models

from django.forms import ModelForm
# Create your models here.


# read the django docs on models:
# https://docs.djangoproject.com/en/dev/topics/db/models/

# model for an SSN
class Social(models.Model):
    '''class representing an SSN'''

    #SSN field with a length of 9
    ssn = models.CharField(max_length=50)

    #methods
    def get_id(self):
        return self.id
    def get_test_ssn(self):
        return self
