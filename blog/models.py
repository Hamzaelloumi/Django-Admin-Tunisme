from django.db import models

class Responsable(models.Model):
   id_responsable = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=20)
   prenom = models.CharField(max_length=20)
   email = models.CharField(max_length= 50)
   password = models.CharField(max_length=20)
   adresse = models.CharField(max_length= 100)

   def __str__(self):
       return self.name +" "+ self.prenom  




class Clinique(models.Model):
   id_clinique = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=20)
   description = models.CharField(max_length=50)
   adresse = models.CharField(max_length= 50)
   Image = models.ImageField(upload_to='cliniques/', blank=True)

   def __str__(self):
       return self.name  

class Sanatorium(models.Model):
   id_sanatorium = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=20)
   description = models.CharField(max_length=50)
   adresse = models.CharField(max_length= 50)
   telephone = models.CharField(max_length= 50)
   Image = models.ImageField(default='default.jpg' , upload_to='sanatoriums')

   def __str__(self):
       return self.name  


class Hote(models.Model):
   id_hote = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=20)
   description = models.CharField(max_length=50)
   adresse = models.CharField(max_length= 50)
   telephone = models.CharField(max_length= 50)
   Image = models.ImageField(default='default.jpg' , upload_to='hotes')

   def __str__(self):
       return self.name  