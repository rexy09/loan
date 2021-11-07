from django.db import models

# Create your models here.

class Sajili(models.Model):
	full_name = models.CharField(max_length=100,)
	phone_number = models.CharField(max_length=15,unique=True)
	balance = models.DecimalField(max_digits=19, decimal_places=2, default=0)
	pin = models.CharField(max_length=100,)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	

	class Meta:
		verbose_name = "Sajili"
		verbose_name_plural = "Sajili"

	def __str__(self):
		return self.full_name

	
class TumaPesa(models.Model):
	no_mtumaji = models.CharField(max_length=13)
	no_mpokeaji = models.CharField(max_length=13)
	kiasi = models.DecimalField(max_digits=19, decimal_places=2, default=0)
	tofauti = models.DecimalField(max_digits=19, decimal_places=2, default=0)
	jumla = models.DecimalField(max_digits=19, decimal_places=2, default=0)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Tuma Pesa"
		verbose_name_plural = "Tuma Pesa"

	def __str__(self):
		return self.no_mtumaji


class Kiwango(models.Model):
	minimum = models.DecimalField(max_digits=19, decimal_places=3, default=0)
	maximum = models.DecimalField(max_digits=19, decimal_places=3, default=0)
	fee = models.DecimalField(max_digits=19, decimal_places=3, default=0)
	tofauti = models.DecimalField(max_digits=19, decimal_places=3, default=0)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Kiwango"
		verbose_name_plural = "Viwango"

	def __str__(self):
		return '{0} - {1}'.format(self.minimum, self.maximum)
