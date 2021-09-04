from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Position(models.Model):
	name = models.CharField(max_length=100, primary_key=True, unique=True)
	date_created = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name


class Employer(MPTTModel):
	name = models.CharField(max_length=200, blank=True, null=True)
	position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True)
	date_employed = models.DateField()
	salary = models.CharField(max_length=150, blank=True, null=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	def __str__(self):
		return self.name

	class MPTTMeta:
		level_attr = 'mptt_level'
		order_insertion_by = ['name']
