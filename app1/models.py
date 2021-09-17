from django.db import models

class CarsGM(models.Model):
	KAROBKA = (
		('avtomat', 'avtomat'),
		('mexanika', 'maxanika')
		)

	MATOR = (
		('1.6', '1.6'),
		('1.8', '1.8'),
		('2.0', '2.0'),
		('2.2', '2.2'),
		('2.4', '2.4'),
		)

	RANGLAR = (
		('oq', 'oq'),
		('qora', 'qora'),
		('qizil', 'qizil'),
		('sariq', 'sariq'),
		('kulrang', 'kulrang'),
		)

	nom = models.CharField(max_length=50)
	karobka = models.CharField(max_length=50, null=True, choices=KAROBKA)
	yili = models.DateField(auto_now=False)
	narxi = models.PositiveIntegerField()
	mator = models.CharField(max_length=20, null=False, choices=MATOR)
	rang = models.CharField(max_length=20, null=True, choices=RANGLAR)
	soni = models.PositiveIntegerField()

	def __str__(self):
		return self.nom.title()
