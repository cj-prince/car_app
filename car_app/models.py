from django.db import models

# Create your models here.
class DateControls(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    abstract = True

class Manufacturer(DateControls):
  name = models.CharField(max_length=200, help_text='holds the name of the car', unique=True)
  
  def __str__(self):
      return self.name

class Feature(DateControls):
  name =  models.CharField(max_length=200, help_text='holds the name of the car', unique=True)
  description = models.TextField(null=True, blank=True)
  
  def __str__(self):
      return self.name
  

class Car(DateControls):
  name = models.CharField(max_length=200, help_text='holds the name of the car')
  model =  models.CharField(max_length=50, choices=(('v8', 'v_8'),('v6', 'v_6'), ('v4', 'v_4')))
  serial_number = models.PositiveBigIntegerField(unique=True)
  manufacture_date =  models.DateTimeField()
  manufacture = models.ForeignKey(Manufacturer, related_name='car_manufacturers', on_delete=models.CASCADE )
  features = models.ManyToManyField(Feature, related_name='car_features')
  
  def __str__(self):
      return f'{self.manufacture.name} {self.name}'


class CarProfile(models.Model):
  year = models.PositiveIntegerField()
  car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='car_profile')
  
  def __str__(self):
      return f'{self.manufacture.name} {self.name}'