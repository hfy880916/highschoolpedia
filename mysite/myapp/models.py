from __future__ import unicode_literals

from django.db import models
from mysite.settings import BASE_DIR
import os

# Create your models here.
class Document(models.Model):
	docfile = models.FileField()