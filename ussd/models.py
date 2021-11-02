from django.db import models

class TumaPesa(models.Model):
	no_mtumaji = models.CharField(max_length=13)
	no_mpokeaji = models.CharField(max_length=13)
	kiasi = models.DecimalField(max_digits=19, decimal_places=2, default=0)
	tofauti = models.IntegerField()
	jumla = models.DecimalField(max_digits=19, decimal_places=2, default=0)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)