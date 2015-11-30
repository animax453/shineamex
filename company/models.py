#python imports
from datetime import datetime

#django imports
from django.db import models

#local imports

#inter app imports

#third party imports

class Company(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True,blank=True)
	created_date = models.DateTimeField(default=datetime.now)

	class Meta:
		verbose_name_plural = "Companies"

	def __unicode__(self):
		return self.name

