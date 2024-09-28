from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class BlogPost:
	title = models.CharField(max_length=50)
	author = User("","","","","")
	body = models.TextField()
	timestamp = models.DateTimeField()
	
	def __init__(self, title, author, body):
		self.title = title
		self.author = author
		self.body = body
		self.timestamp = datetime.now()