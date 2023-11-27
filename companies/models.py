from django.db import models

class Company(models.Model):
    siret_number = models.CharField("numéro de SIRET", max_length=14)
    name = models.CharField("nom de l'entreprise", max_length=20)
    def __str__(self):
        return self.name
    def nic_number(self):
        return str(self.siret_number)[9:]
    def siren_number(self):
        return str(self.siret_number)[:9]

class Employee(models.Model):
    employer = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField("prénom", max_length=50)
    last_name = models.CharField("nom", max_length=50)
    date_of_birth = models.DateField("date de naissance")
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
