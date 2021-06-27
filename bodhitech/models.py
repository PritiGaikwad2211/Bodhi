from django.db import models

# Create your models here.
class carousel (models.Model):
    Heading=models.CharField(max_length=50,null=True)
    Description=models.CharField(max_length=400,null=True)
    Img=models.ImageField(upload_to='img/carousel',null=True)
    
    submittedat=models.DateTimeField(auto_now_add=True,null=True)
    updatedat=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'carousel'
    def __str__(self):
            return self.Heading_1
           

class section (models.Model):
    heading=models.CharField(max_length=50,null=True)
    Title=models.CharField(max_length=50,null=True)
    content=models.CharField(max_length=400,null=True)
    gif=models.ImageField(upload_to=('img/section'),null=True)
    
    submittedat=models.DateTimeField(auto_now_add=True,null=True)
    updatedat=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'section'
    def __str__(self):
        return self.heading 

class clients (models.Model):
    heading=models.CharField(max_length=50,null=True)
    img=models.ImageField(upload_to=('img/carousel'),null=True)
    
    submittedat=models.DateTimeField(auto_now_add=True,null=True)
    updatedat=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'clients'
    def __str__(self):
        return self.heading 

class about (models.Model):
    heading=models.CharField(max_length=50,null=True)
    content=models.TextField(max_length=300,null=True)
    
    img=models.ImageField(upload_to=('img/carousel'),null=True)
    submittedat=models.DateTimeField(auto_now_add=True,null=True)
    updatedat=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'about'
    def __str__(self):
            return self.heading 



