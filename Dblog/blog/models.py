from django.db import models
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField
# Create your models here.

class Tag(models.Model):
	tag_name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.tag_name

		
class Blog(models.Model):
	title = models.CharField(max_length = 50)
	original_date = models.DateField()
	update_date = models.DateField()
	content = MarkdownField()
	description = models.TextField()
	tag = models.ManyToManyField(Tag)

	def __unicode__(self):
		return self.title



class User(models.Model):
	user_name = models.CharField(max_length=20)
	user_email = models.EmailField(blank =True)

	def __unicode__(self):
		return self.user_name

