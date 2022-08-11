from distutils.command.upload import upload
from operator import mod
from statistics import mode
from django.db import models

# Create your models here.

class carousel(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(null=True, blank=True, upload_to='images/')
    caption=models.CharField(max_length=250)
    button=models.BooleanField(default=False)
    button_title=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    
class product(models.Model):
    brand_name=models.CharField(max_length=50)
    product_name=models.CharField(max_length=50)
    product_image= models.ImageField(null=True, blank=True, upload_to='images/')
    product_description= models.TextField(max_length=300)
    reviews=models.IntegerField()
    stars=models.CharField(max_length=5)

    def __str__(self):
        return self.product_name

class contacts(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    query=models.TextField()

    def __str__(self):
        return self.name

    
class data(models.Model):
    Item_Name= models.CharField(max_length=250)
    Stock_Group= models.CharField(max_length=250,null=True, blank=True)
    Stock_Category= models.CharField(max_length=250,null=True, blank=True)
    Base_Unit_Qty= models.IntegerField(null=True, blank=True)
    Rate= models.FloatField(null=True, blank=True)
    GST_Applicable= models.CharField(default='True',max_length=100)
    HSN_SAC_Code= models.CharField(max_length=250,null=True, blank=True)
    IGST_Rate=models.IntegerField(null=True, blank=True)
    Reporting_UQC=models.CharField(max_length=250,null=True, blank=True)
    MRP_Rate=models.FloatField(null=True, blank=True)
    Manufracturing_Date=models.CharField(max_length=250,null=True, blank=True)
    Image_Link=models.TextField(max_length=15000,null=True, blank=True)

    def __str__(self):
        return self.Item_Name

class cards(models.Model):
    title=models.CharField(max_length=70,null=True, blank=True)
    image=models.ImageField(null=True, blank=True, upload_to='images/')
    description=models.CharField(max_length=350)


class about(models.Model):
    title=models.CharField(max_length=70,null=True, blank=True)
    image=models.ImageField(null=True, blank=True, upload_to='images/')
    description=models.TextField(null=True, blank=True,max_length=350)
