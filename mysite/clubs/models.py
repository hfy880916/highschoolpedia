# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mysite.settings import BASE_DIR
import os

# Create your models here.
	
class Article(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	atribute = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class images(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE, default = None)
	image = models.ImageField(upload_to = 'clubs')